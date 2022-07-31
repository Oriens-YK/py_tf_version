import cv2
import glob
import numpy as np

count = 0
path = glob.glob(r"D:\code\python\GAN\archive\train\*.jpg")
tar_images, src_images = [], []
for directory_path in path:
    img = cv2.imread(directory_path, cv2.IMREAD_COLOR)
    print(type(img))
    print(img.shape)
    imgtar = np.array(img[:,:600])
    imgsrc = np.array(img[:,600:])
    imgsrc = cv2.resize(imgsrc, (SIZE_Y, SIZE_X))
    imgtar = cv2.resize(imgtar, (SIZE_Y, SIZE_X))
    tar_images.append(list(imgtar))
    src_images.append(list(imgsrc))
    if count == 1:
        break
    count+=1
    

tar_images = np.array(tar_images)
# print(tar_images.shape)
# cv2.imshow("cropped", tar_images[0])
# cv2.waitKey(0)
src_images = np.array(src_images)
# print(src_images.shape)
# cv2.imshow("cropped", src_images[0])
# cv2.waitKey(0)
# print(tar_images[0])