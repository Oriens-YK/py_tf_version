import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import models
import tensorflow.keras.backend as K
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions

VGG16_model = tf.keras.applications.VGG16(include_top=True,weights='imagenet')
VGG16_model.summary()

def prepocess(x):
    x = tf.io.read_file(x)
    x = tf.image.decode_jpeg(x, channels=3)
    x = tf.image.resize(x, [224,224])
    x =tf.expand_dims(x, 0) # 擴維
    x = preprocess_input(x)
    return x


img_path='dog.jpg'
img=prepocess(img_path)
Predictions = VGG16_model.predict(img)
print('Predicted:', decode_predictions(Predictions, top=3)[0])


last_conv_layer = VGG16_model.get_layer('block5_pool')
heatmap_model =models.Model([VGG16_model.inputs], [last_conv_layer.output, VGG16_model.output])


with tf.GradientTape() as gtape:
    conv_output, Predictions = heatmap_model(img)
    prob = Predictions[:, np.argmax(Predictions[0])] # 最大可能性類別的預測概率
    grads = gtape.gradient(prob, conv_output)  # 類別與卷積層的梯度 (1,14,14,512)
    pooled_grads = K.mean(grads, axis=(0,1,2)) # 特徵層梯度的全局平均代表每個特徵層權重
    
heatmap = tf.reduce_mean(tf.multiply(pooled_grads, conv_output), axis=-1) #權重與特徵層相乘，512層求和平均


heatmap = np.maximum(heatmap, 0)
max_heat = np.max(heatmap)
if max_heat == 0:
    max_heat = 1e-10
heatmap /= max_heat


original_img=cv2.imread(img_path)
heatmap1 = cv2.resize(heatmap[0], (original_img.shape[1], original_img.shape[0]), interpolation=cv2.INTER_CUBIC)

heatmap1 = np.maximum(heatmap1,0)
heatmap1 = heatmap1/np.max(heatmap1)

heatmap1 = np.uint8(255*heatmap1)
heatmap1 = cv2.applyColorMap(heatmap1, cv2.COLORMAP_JET)
frame_out=cv2.addWeighted(original_img,0.5,heatmap1,0.5,0)
# frame_out = heatmap1*0.4 + original_img
cv2.imwrite('./heatmap.jpg', frame_out)

plt.figure()
plt.imshow(frame_out)