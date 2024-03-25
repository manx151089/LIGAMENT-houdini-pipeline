"""
import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH  = 'D:/stop.jpg'

reader = easyocr.Reader(['en'],gpu=False)
result = reader.readtext(IMAGE_PATH)
result

"""

import pytesseract
import os

from PIL import Image

# Load an image
image_path = 'D:\stop.jpg'
image = Image.open(image_path)
print(os.path.exists(image_path))
# Perform OCR
text = pytesseract.image_to_string(image)
print(text)

