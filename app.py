import numpy as np
from imageio import imread,imwrite
import cv2

img = imread('day.jpg')

arr = img *np.array([0.3,0.3,0.4])  #[0.1,0.2,0.5] og array
arr2 = (255*arr/arr.max()).astype(np.uint8)
imwrite('night.png',arr2)

img2 = cv2.imread('night.png')
gamma = 3 #for the darkness like a night

gamma_img = np.array(255*(img2/255)**gamma,dtype= 'uint8')

cv2.imwrite('nigh_final.png',gamma_img)
print("Conversion done!")
