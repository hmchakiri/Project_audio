import matplotlib.pyplot as plt
import cv2
import numpy as np

def printMatrix(s):

    # Do heading
    print("     ", end="")
    for j in range(len(s[0])):
        print("%5d " % (j+1), end="")
    print()
    print("     ", end="")
    for j in range(len(s[0])):
        print("------", end="")
    print()
    # Matrix contents
    for i in range(len(s)):
        print("%3d |" % (i+1), end="") # Row nums
        for j in range(len(s[0])):
            print("%5.1f " % (s[i][j]), end="")
        print()  
        
img = np.array(([\
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]), np.float32)*255

plt.figure()
plt.title('Original image')
plt.imshow(img, cmap='gray', vmin=0, vmax=255)

ContourExtraction = np.array(([\
    [-1, -1, -1],  \
    [-1, 8, -1], \
    [-1, -1, -1]]), np.float32)/9
ContourEnhancement = np.array(([\
    [-1, -1, -1],  \
    [-1, 9, -1], \
    [-1, -1, -1]]), np.float32)/9

selectedFilter = ContourExtraction

output=abs(cv2.filter2D(img, -1, selectedFilter))
#output=cv2.filter2D(output, -1, selectedFilter). # apply twice

plt.figure()
plt.title('Filtered image')
plt.imshow(output, cmap='gray', vmin=0, vmax=255)

printMatrix(output)
