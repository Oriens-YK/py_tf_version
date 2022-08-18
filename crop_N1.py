import cv2
import math
import numpy as np
path = 'N1.jpg'
path_O = 'N1O.jpg'

image = cv2.imread(path)
image_O = cv2.imread(path_O)
image_O_2 = cv2.imread(path_O)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
X = image.shape[1]
Y = image.shape[0]
up_blue = [100, 100, 46]
down_blue = [124,255, 255]

up_red = [156, 43, 46]
down_red  = [180,255, 255]

img_Y = 0
all_blue_X = []
all_blue_Y = []
all_red_X = []
all_red_Y = []

for i in range(X*Y):
    if i%X == 0:
        img_Y+=1
    
    if up_blue[0]<hsv[img_Y-1,i%X][0]<down_blue[0] and up_blue[1]<hsv[img_Y-1,i%X][1]<down_blue[1] and up_blue[2]<hsv[img_Y-1,i%X][2]<down_blue[2]:
        # print(i%X, img_Y-1)
        all_blue_X.append(i%X)
        all_blue_Y.append(img_Y-1)
        
    if up_red[0]<hsv[img_Y-1,i%X][0]<down_red[0] and up_red[1]<hsv[img_Y-1,i%X][1]<down_red[1] and up_red[2]<hsv[img_Y-1,i%X][2]<down_red[2]:
        all_red_X.append(i%X)
        all_red_Y.append(img_Y-1)
        
        

min_rectangle_X = min(all_blue_X)
min_rectangle_Y = min(all_blue_Y)
rectangle_w = max(all_blue_X)-min_rectangle_X
rectangle_h = max(all_blue_Y)-min_rectangle_Y

print(min_rectangle_X, min_rectangle_Y, rectangle_w, rectangle_h)

pix = 2
crop_img = image_O[min_rectangle_Y-pix:min_rectangle_Y+rectangle_h+pix, min_rectangle_X-pix:min_rectangle_X+rectangle_w+pix]

image_O[min_rectangle_Y-pix:min_rectangle_Y+rectangle_h+pix, min_rectangle_X-pix:min_rectangle_X+rectangle_w+pix] = np.ones_like(crop_img)*255


min_ellipse_X = min(all_red_X)
min_ellipse_Y = min(all_red_Y)
max_ellipse_X = max(all_red_X)
max_ellipse_Y = max(all_red_Y)

pix = 3
center_X = abs(int((min_ellipse_X+max_ellipse_X)/2))
center_Y = abs(int((min_ellipse_Y+max_ellipse_Y)/2))
X_length = int(abs(center_X-min_ellipse_X))
Y_length = int(abs(center_Y-min_ellipse_Y))

cv2.ellipse(image_O,(center_X,center_Y),(X_length-pix,Y_length-pix),0,0,360,(0,0,0),-1)

img_Y = 0
for i in range(X*Y):
    gray = cv2.cvtColor(image_O, cv2.COLOR_RGB2GRAY)

    if i%X == 0:
        img_Y+=1
    if gray[img_Y-1][i%X]<127:
        image_O_2[img_Y-1][i%X] = image_O_2[img_Y-1, i%X]
    else:
        image_O_2[img_Y-1][i%X] = 255
        
        
# cv2.imshow('gray', gray)
# cv2.waitKey(0)
# cv2.imwrite('image.jpg', image_O)
# cv2.imshow('image', image_O)
# cv2.waitKey(0)
# cv2.imwrite('crop_img.jpg', crop_img)
# cv2.imshow('crop_img', crop_img)
# cv2.waitKey(0)
cv2.imwrite('image_O_2.jpg', image_O_2)
cv2.imshow('image_O_2', image_O_2)
cv2.waitKey(0)
