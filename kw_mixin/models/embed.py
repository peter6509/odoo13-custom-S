import re
import io
import base64
import logging
import requests

from PIL import Image

from werkzeug import urls
from odoo import models, api, fields, _
from odoo.addons.http_routing.models.ir_http import url_for
from odoo.http import request

_logger = logging.getLogger(__name__)


# pylint: disable=inconsistent-return-statements
class EmbedMixin(models.AbstractModel):
    _name = 'kw.embed.mixin'
    _description = 'Embed Mixin'

    kw_embed_type = fields.Selection(
        string='Type', required=True, default='document',
        selection=[
            ('infographic', _('Infographic')), ('webpage', _('Web Page')),
            ('presentation', _('Presentation')), ('document', _('Document')),
            ('video', _('Video')), ], )
    kw_embed_datas = fields.Binary(
        string='Content', attachment=True, )
    kw_embed_url = fields.Char(
        string='Document URL', help='Youtube or Google Document URL')
    kw_embed_document_id = fields.Char(
        help='Youtube or Google Document ID')
    kw_embed_mime_type = fields.Char()

    kw_embed_code = fields.Text(
        compute='_compute_kw_embed_code', )

    @api.model
    def create(self, values):
        if values.get('kw_embed_url') and not values.get(
                'kw_embed_document_id'):
            doc_data = self._parse_document_url(
                values['kw_embed_url']).get('values', dict())
            for key, value in doc_data.items():
                values.setdefault(key, value)

        return super().create(values)

    def write(self, values):
        if values.get('kw_embed_url') and \
                values['kw_embed_url'] != self.kw_embed_url:
            doc_data = self._parse_document_url(
                values['kw_embed_url']).get('values', dict())
            for key, value in doc_data.items():
                values.setdefault(key, value)

        return super().write(values)

    def _parse_document_url(self, url, only_preview_fields=False):
        document_source, document_id = self._find_document_data_from_url(url)
        if document_source and hasattr(
                self, '_parse_%s_document' % document_source):
            attr = '_parse_%s_document' % document_source
            return getattr(self, attr)(document_id, only_preview_fields)
        return {'error': _('Unknown document')}

    @api.depends('kw_embed_document_id', 'kw_embed_type', 'kw_embed_mime_type')
    def _compute_kw_embed_code(self):
        _logger.info('_compute_kw_embed_code')
        if request and request.httprequest.url_root:
            base_url = request and request.httprequest.url_root
        else:
            base_url = self.env['ir.config_parameter'].sudo().get_param(
                'web.base.url')
        if base_url[-1] == '/':
            base_url = base_url[:-1]
        for record in self:
            is_document = \
                record.kw_embed_datas and \
                (not record.kw_embed_document_id or
                 record.kw_embed_type in ['document', 'presentation'])
            _logger.info(is_document)
            if is_document:
                slide_url = base_url + url_for(
                    '/slides/embed/%s?page=1' % record.id)
                record.kw_embed_code = \
                    '<iframe src="%s" class="o_wslides_iframe_viewer" ' \
                    'allowFullScreen="true" height="%s" width="%s" ' \
                    'frameborder="0"></iframe>' % (slide_url, 315, 420)
            elif record.kw_embed_type == 'video' and \
                    record.kw_embed_document_id:
                if not record.kw_embed_mime_type:
                    # embed youtube video
                    query = urls.url_parse(record.kw_embed_url).query
                    query = query + '&theme=light' if query else 'theme=light'
                    record.kw_embed_code = \
                        '<iframe src="//www.youtube.com/embed/{}?{}" ' \
                        'allowFullScreen="true" frameborder="0" ' \
                        'width="560" height="315"></iframe>' \
                        ''.format(record.kw_embed_document_id, query)
                else:
                    # embed google doc video
                    record.kw_embed_code = \
                        '<iframe src="//drive.google.com/file/d/%s/preview" ' \
                        'allowFullScreen="true" frameborder="0"></iframe>' \
                        '' % record.kw_embed_document_id
            else:
                record.kw_embed_code = False
    # --------------------------------------------------
    # Parsing methods
    # --------------------------------------------------

    @api.model
    def _fetch_data(self, base_url, params, content_type=False):
        result = {'values': dict()}
        try:
            response = requests.get(base_url, timeout=3, params=params)
            response.raise_for_status()
            if content_type == 'json':
                result['values'] = response.json()
            elif content_type in ('image', 'pdf'):
                result['values'] = base64.b64encode(response.content)
            else:
                result['values'] = response.content
        except requests.exceptions.HTTPError as e:
            result['error'] = e.response.content
        except requests.exceptions.ConnectionError as e:
            result['error'] = str(e)
        return result

    def _find_document_data_from_url(self, url):
        url_obj = urls.url_parse(url)
        if url_obj.ascii_host == 'youtu.be':
            return ('youtube', url_obj.path[1:] if url_obj.path else False)
        if url_obj.ascii_host in (
                'youtube.com', 'www.youtube.com', 'm.youtube.com'):
            v_query_value = url_obj.decode_query().get('v')
            if v_query_value:
                return ('youtube', v_query_value)
            split_path = url_obj.path.split('/')
            if len(split_path) >= 3 and split_path[1] in ('v', 'embed'):
                return ('youtube', split_path[2])

        expr = re.compile(
            r'(^https:\/\/docs.google.com|^https:\/\/drive.google.com'
            r').*\/d\/([^\/]*)')
        arg = expr.match(url)
        document_id = arg.group(2) if arg else False
        if document_id:
            return 'google', document_id

        return None, False

    def _parse_document_url(self, url, only_preview_fields=False):
        document_source, document_id = self._find_document_data_from_url(url)
        if document_source and hasattr(
                self, '_parse_%s_document' % document_source):
            attr = '_parse_%s_document' % document_source
            return getattr(self, attr)(document_id, only_preview_fields)
        return {'error': _('Unknown document')}

    def _parse_youtube_document(self, document_id, only_preview_fields):
        key = self.env['website'].get_current_website(
        ).website_slide_google_app_key
        fetch_res = self._fetch_data(
            'https://www.googleapis.com/youtube/v3/videos', {
                'id': document_id,
                'key': key,
                'part': 'snippet,contentDetails',
                'fields': 'items(id,snippet,contentDetails)'}, 'json')
        if fetch_res.get('error'):
            return fetch_res

        values = {'kw_embed_type': 'video',
                  'kw_embed_document_id': document_id}
        items = fetch_res['values'].get('items')
        if not items:
            return {'error': _('Please enter valid Youtube or Google Doc URL')}
        youtube_values = items[0]

        if youtube_values.get('snippet'):
            snippet = youtube_values['snippet']
            if only_preview_fields:
                values.update({
                    'url_src': snippet['thumbnails']['high']['url'],
                    'title': snippet['title'],
                    'description': snippet['description']
                })

                return values

            values.update({
                'kw_embed_mime_type': False,
            })
        return {'values': values}

    @api.model
    def _parse_google_document(self, document_id, only_preview_fields):
        def get_kw_embed_type(vals):
            # TDE FIXME: WTF ??
            kw_embed_type = 'presentation'
            if vals.get('image_1920'):
                image = Image.open(
                    io.BytesIO(base64.b64decode(vals['image_1920'])))
                width, height = image.size
                if height > width:
                    return 'document'
            return kw_embed_type

        params = {}
        params['projection'] = 'BASIC'
        if 'google.drive.config' in self.env:
            access_token = self.env['google.drive.config'].get_access_token()
            if access_token:
                params['access_token'] = access_token
        if not params.get('access_token'):
            params['key'] = self.env['website'].get_current_website(
            ).website_slide_google_app_key

        fetch_res = self._fetch_data(
            'https://www.googleapis.com/drive/v2/files/%s'
            '' % document_id, params, "json")
        if fetch_res.get('error'):
            return fetch_res

        google_values = fetch_res['values']
        if only_preview_fields:
            return {
                'url_src': google_values['thumbnailLink'],
                'title': google_values['title'],
            }

        values = {
            'kw_embed_mime_type': google_values['mimeType'],
            'kw_embed_document_id': document_id,
        }
        if google_values['mimeType'].startswith('video/'):
            values['kw_embed_type'] = 'video'
        elif google_values['mimeType'].startswith('image/'):
            values['kw_embed_datas'] = values['image_1920']
            values['kw_embed_type'] = 'infographic'
        elif google_values['mimeType'].startswith(
                'application/vnd.google-apps'):
            values['kw_embed_type'] = get_kw_embed_type(values)
            if 'exportLinks' in google_values:
                values['datas'] = self._fetch_data(
                    google_values['exportLinks']['application/pdf'],
                    params, 'pdf')['values']
        elif google_values['mimeType'] == 'application/pdf':
            values['kw_embed_datas'] = self._fetch_data(
                google_values['webContentLink'], {}, 'pdf')['values']
            values['kw_embed_type'] = get_kw_embed_type(values)

        return {'values': values}
