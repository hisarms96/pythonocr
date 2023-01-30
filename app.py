# To support Korean, 
# > sudo apt-get install tesseract-ocr-kor
import pytesseract
from PIL import Image

import os
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata'

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
### r'/usr/share/tesseract-ocr'

img = Image.open('traders_receipt.jpg')
result = pytesseract.image_to_string(img, lang='kor')
print(result)