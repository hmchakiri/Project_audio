# Image stats and image processing
# works on google colab
import common #some useful opencv functions
# 1st part
# Download the test image and utils files
!wget --no-check-certificate \
    https://i.pinimg.com/474x/00/58/3e/00583edcee184f3c677fb613645f37f8.jpg \
    -O elephant.jpg
!wget --no-check-certificate \
    https://raw.githubusercontent.com/computationalcore/introduction-to-opencv/master/utils/common.py \
    -O common.py
# these imports let you use opencv
import matplotlib.pyplot as plt

import cv2
import numpy as np
img = cv2.imread('elephant.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rows,cols = img.shape[:2]

plt.figure()
plt.title('Original image')
plt.imshow(img, cmap='gray', vmin=0, vmax=255)


#identity
kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
output=cv2.filter2D(img,-1,kernel_identity)
plt.figure()
plt.title('Unity filter')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)


#blur
kernel_3x3 = np.ones((3,3),np.float32) / 9.0
output=cv2.filter2D(img,-1,kernel_3x3) 
plt.figure()
plt.title('Please identify filter')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#larger blur
kernel_5x5 = np.ones((5,5),np.float32) / 25.0
output=cv2.filter2D(img,-1,kernel_5x5)
plt.figure()
plt.title('Please identify filter')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#motion blur
size=15
kernel_motion_blur = np.zeros((size,size))
kernel_motion_blur[int((size-1)/2),:] = np.ones(size)
kernel_motion_blur = kernel_motion_blur /  size
output=cv2.filter2D(img,-1,kernel_motion_blur)
plt.figure()
plt.title('Motion blur')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#sharpen
kernel_sharpen_1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
output1=cv2.filter2D(img,-1,kernel_sharpen_1)
plt.figure()
plt.title('Sharpening')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#more shapening
kernel_sharpen_2 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
output2=cv2.filter2D(img,-1,kernel_sharpen_2)
plt.figure()
plt.title('Excessive sharpening')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#edge enhancement
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]])/8.0
output3=cv2.filter2D(img,-1,kernel_sharpen_3)
plt.figure()
plt.title('Edge Enhancement')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#emboss
kernel_emboss1=np.array([[0,-1,1],[1,0,-1],[1,1,0]])
output=cv2.filter2D(gray,-1,kernel_emboss1)+128
plt.figure()
plt.title('Emboss1')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#emboss2
kernel_emboss2=np.array([[-1,-1,0],[-1,0,11],[0,1,1]])
output=cv2.filter2D(gray,-1,kernel_emboss2)+128
plt.figure()
plt.title('Emboss2')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#emboss3
kernel_emboss3=np.array([[1,0,0],[0,0,0],[0,0,-1]])
output=cv2.filter2D(gray,-1,kernel_emboss3)+128
plt.figure()
plt.title('Emboss3')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#Sobel
sobel_horizontal = cv2.Sobel(img,cv2.CV_64F, 1,0,ksize=5)
plt.figure()
plt.title('Sobel horizontal')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#Sobel2
sobel_vertical = cv2.Sobel(img,cv2.CV_64F, 1,0,ksize=5)
plt.figure()
plt.title('Sobel vertical')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#erode
kernel_erode=np.ones((5,5),np.uint8)
img_erosion = cv2.erode(img,kernel_erode,iterations = 1)
plt.figure()
plt.title('Erode')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#dilate
img_dilatation = cv2.dilate(img,kernel_erode,iterations = 1)
plt.figure()
plt.title('Dilate')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#vignette
kernel_gauss_x= cv2.getGaussianKernel(cols,200)
kernel_gauss_y = cv2.getGaussianKernel(rows,200)
kernel = kernel_gauss_y * kernel_gauss_x.T
mask=255*kernel/np.linalg.norm(kernel)
output=np.copy(img)
for i in range(3):
  output[:,:,i]=output[:,:,i] * mask
plt.figure()
plt.title('Vignette')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

#shifted vignette
kernel_gauss_x= cv2.getGaussianKernel(int(1.5*cols),200)
kernel_gauss_y = cv2.getGaussianKernel(int(1.5*rows),200)
kernel = kernel_gauss_y * kernel_gauss_x.T
mask=255*kernel/np.linalg.norm(kernel)
mask = mask[int(0.5*rows):,int(0.5*cols):]
output=np.copy(img)
for i in range(3):
  output[:,:,i]=output[:,:,i] * mask
plt.figure()
plt.title('Shifted Vignette')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)
