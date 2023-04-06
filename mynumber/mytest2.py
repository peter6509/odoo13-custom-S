# -*- coding: utf-8 -*-
# Author : Peter Wu

from PIL import Image
import pytesseract
img = Image.open('number7.jpg')
text = pytesseract.image_to_string(img,lang='chi_tra')
print(text)