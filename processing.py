import cv2 as cv; 
import numpy as np; 
from matplotlib import pyplot as plt; 
import time; 


img = cv.imread("test4.png"); 
#img2 = cv.GaussianBlur(img, (11,11), sigmaX=100, sigmaY=100); 
# img2 = cv.GaussianBlur(img, (5, 5), sigmaX=0.8, sigmaY=0.8); 
# img3 = cv.Canny(img2, 50, 100); 

# #50, 220 for aurelion

# #cv.imshow("image", img3); 
# plt.imshow(img3); 
# plt.show(); 
#cv.waitKey(0); 


#cv.destroyAllWindows(); 

####
#img2 = [1/20, 1/100, 1] * img; 
# img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY); 
edges = cv.Canny(img, 50, 100); 
features = []; 
# plt.imshow(img2); 
# plt.show()

# start = time.time(); 
# e = edges == 255; 
# edges[e] = 50; 
# # np.where(edges == 255, 50, 0); 
# print(time.time() - start); 

for row in range(0, edges.shape[0]):
    for col in range(0, edges.shape[1]): 
        if edges[row, col] == 255:
            edges[row, col] = 50; 

cv.imshow("image", edges); 
cv.waitKey(0);
cv.destroyAllWindows();


def lineTracking(row, col, feat_index = -1): 

    neighbors = []; 
    edgePixels = [];  

    if feat_index == -1:
        feat_index = len(features); 
        features[feat_index] = np.zeros((edges.shape[0], edges.shape[1])); 
    #otherwise, it's assummed feat_index < len(features)
    #  (i.e., feature already exists); 

    #this is a normal pixel 
    if (row < (edges.shape[0] - 1) and col < (edges.shape[1] - 1)):
        neighbors = [
            [row, col + 1], 
            [row + 1, col - 1], 
            [row + 1, col],
            [row + 1, col +1]]; 
    elif (row < (edges.shape[0] - 1)):  #side border pixel 
        neighbors = [
            [row + 1, col - 1],
            [row + 1, col]
        ]; 
    elif (col < (edges.shape[1] - 1)): #bottom border pixel 
        neighbors = [row, col + 1]; 
    #else, the pixel is at the very corner, it has no valid neighbors. 

    for neighbor in neighbors:
        if (edges[neighbor[0]][neighbor[1]] == 255):
            edgePixels.append(neighbor); 
    
    mainBranchUsed = False; 
    for pixel in edgePixels: 



        if not mainBranchUsed:
            lineTracking(pixel[0], pixel[1], feat_index); 
            mainBranchUsed = True; 
        
        lineTracking(pixel[0], pixel[1]); 

        #lineTracking(pixel[0], pixel[1], feat_index + i)

        #track_line(row, column, direction, global_dir, feat_index)


def track_line(row, col, global_dir, local_dir = 0, fet_index = -1):

    neighbors = []; 

    if (local_dir == 0):
        neighbors = [
            [row, col + 1],
            [row + 1, col - 1],
            [row + 1, col], 
            [row + 1, col + 1]
        ]
    elif (local_dir == 1):
        neighbors = [row, col + 1]; 
    elif (local_dir == 2):
        neighbors = [
            [row, col + 1],
            [row - 1, col + 1],
            [row - 1, col]
        ]
    pass; 


#Big update:
# Las direcciones se mantienen hasta llegar a esquinas. Las esquinas pueden tomar todas las direcciones. 
# Los pixeles del vecindario válidos cambian según la dirección. 
# La dirección local debe concordar con la dirección global del trayecto (izquierda o derecha).
# A pesar de que la dirección se mantenga, se lee el vecindario completo en busca de linkers. 
# Los linkers se agregan a una matriz adicional del mismo tamaño de la imagen. Un linker se representa con un 1.
# Todas las demás casillas son marcadas con un 0. 

#
#       | 4 | 3 | 2 |
#       | 5 |   | 1 |
#       | 6 | 7 | 8 |
#       default = 0; 



# Iter over image 
# 
#
#
