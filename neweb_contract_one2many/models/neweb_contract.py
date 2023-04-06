
from odoo import models, fields, api

class NewebContract(models.Model):
	_inherit = 'neweb_contract.contract'

	# Demo method that will delete your sale orde line as you select and press delete
	@api.model
	def delete_contract_lines(self, selected_ids):
		contractline_sudo = self.env['neweb_contract.contract.line'].sudo()
		contract_lines = contractline_sudo.browse(selected_ids)
		for line in contract_lines:
			line.unlink()
		return True