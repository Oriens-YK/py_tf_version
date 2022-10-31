import pytesseract
import numpy as np
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


fileName = '2.jpg'
img1 = cv2.imread(fileName)
cv2.imshow(fileName, img1)
cv2.waitKey()

text = pytesseract.image_to_string(img1)
print(text)