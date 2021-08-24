# Image stats and image processing
# works on google colab
import common #some useful opencv functions

# 1st part
# Download the test image and utils files
!wget --no-check-certificate \
    https://www.therobotreport.com/wp-content/uploads/2020/05/Photoneo_depalletization-1024x772.jpg \
    -O robot.jpg
!wget --no-check-certificate \
    https://raw.githubusercontent.com/computationalcore/introduction-to-opencv/master/utils/common.py \
    -O common.py
# these imports let you use opencv
import matplotlib.pyplot as plt
import cv2
import numpy as np

def processImage(image):
    image = cv2.imread(image)
    image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
    return image


img = processImage('robot.jpg')
plt.figure()
plt.title('Original image')
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

gaussianBlurKernel = np.array(([\
    [1, 2, 1], \
    [2, 4, 2], \
    [1, 2, 1]]), np.float32)/9
sharpenKernel = np.array(([\
    [0, -1, 0],  \
    [-1, 9, -1], \
    [0, -1, 0]]), np.float32)/9
mean3BlurKernel = np.array(([\
    [1, 1, 1],  \
    [1, 1, 1], \
    [1, 1, 1]]), np.float32)/9
mean5BlurKernel = np.array(([\
    [1, 1, 1, 1, 1],  \
    [1, 1, 1, 1, 1],  \
    [1, 1, 1, 1, 1],  \
    [1, 1, 1, 1, 1],  \
    [1, 1, 1, 1, 1]]), np.float32)/25

selectedFilter = mean5BlurKernel

output=cv2.filter2D(img, -1, selectedFilter)
#output=cv2.filter2D(output, -1, selectedFilter). # apply twice

plt.figure()
plt.title('Filtered image')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)
