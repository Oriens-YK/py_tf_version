# import pytesseract
# import numpy as np
# import cv2
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# fileName = '2.jpg'
# img1 = cv2.imread(fileName)
# cv2.imshow(fileName, img1)
# cv2.waitKey()

# text = pytesseract.image_to_string(img1)
# print(text)

import matplotlib.pyplot as plt
import keras_ocr

# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline()

# Get a set of three example images
img = [
    keras_ocr.tools.read (img) for img in ['3.jpg',
                                          '2.jpg',]
]


# Each list of predictions in prediction_groups is a list of
# (word, box) tuples.
prediction_groups = pipeline.recognize(images=img)

fig, axs = plt.subplots(nrows=len(img), figsize=(20, 20))
count = 0
for ax, image, predictions in zip(axs, img, prediction_groups):
    count+=1
    keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
plt.savefig('./test.jpg')
