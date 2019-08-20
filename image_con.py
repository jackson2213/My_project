import cv2
import numpy as np
import pandas as pd


img1 = cv2.imread('./1.png')
img2 = cv2.resize(cv2.imread('./2.png'))
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# ====使用numpy的数组矩阵合并concatenate======

def  image_concat(image1,image2,blank_pix=10,axis=1):
    #** blank_pix 两张图之间间隙是多少像素
    # axis 默认是1表示图片横向拼接，纵向拼接改为0
    #返回得是拼接后得图像

     if image1.shape[0]!=image2.shape[0] or image1.shape[1]!=image2.shape[1]:
         return 'image shape must euqal!'

     if axis==1:
         blank_array=np.full((image1.shape[0], blank_pix), 255)
     else:
         blank_array=np.full((blank_pix,image1.shape[1]), 255)
     #image = np.concatenate((gray1, gray2))  # 纵向连接=np.vstack((gray1, gray2))
     image = np.concatenate([gray1,blank_array,gray2], axis=axis)  #横向拼接,如果多于两张图片，
     # 可以直接再参数加:[image1,gray1,blank_array,gray2,image3,blank_array,image4], blank_array是两张图片中得空白间隙，多少像素可以更改，默认设置是10
     return image


result_image=image_concat(gray2,gray1)
