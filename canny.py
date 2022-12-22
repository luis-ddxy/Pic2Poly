import cv2 as cv; 
import numpy as np; 
from matplotlib import pyplot as plt; 
import time; 

img = cv.imread("test4.png"); 
#img = cv.GaussianBlur(img, (5,5), sigmaX=0.8, sigmaY=0.8)

edges = cv.Canny(img, 50, 100); 
edgesBool = np.where(edges == 255, True, False); 


for row in range(edges.shape[0] - 1):
    for col in range(edges.shape[1]- 1):

        if(edgesBool[row][col] and edgesBool[row][col + 1] and 
        edgesBool[row + 1][col+ 1] and edgesBool[row + 1][col]):
            edgesBool[row][col] = 0; 
            edgesBool[row + 1][col + 1] = 0; 

edgesNorm = np.where(edgesBool, 255, 0); 

plt.subplot(1, 2, 1); 
plt.imshow(edges); 
plt.subplot(1, 2, 2); 
plt.imshow(edgesNorm); 
plt.show(); 
