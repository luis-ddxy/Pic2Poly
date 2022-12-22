import cv2 as cv; 
import numpy as np; 
from matplotlib import pyplot as plt; 
import time; 

binary_mat = []; 
img = np.zeros((116, 116));  

for i in range(256): 
    binary_arr = np.array(list(np.binary_repr(i, width=8))); 
    binary_arr = np.where(binary_arr == "1", True, False); 
    binary_mat.append(binary_arr); 

for j in range(16):
    corner_y = 5 * j + 2 * (j + 1); 
    for i in range(16): 
        corner_x = 5 * i + 2 * (i + 1); 

        binary_mat_index = 16 * j + i; 
        arr = binary_mat[binary_mat_index]; 

        img[corner_y + 2][corner_x + 2] = 255; 

        if(arr[0]):
            img[corner_y + 2][corner_x + 3] = 255; 
            img[corner_y + 2][corner_x + 4] = 255;
        if(arr[1]): 
            img[corner_y + 1][corner_x + 3] = 255; 
            img[corner_y + 0][corner_x + 4] = 255; 
        if(arr[2]):
            img[corner_y + 1][corner_x + 2] = 255; 
            img[corner_y + 0][corner_x + 2] = 255; 
        if(arr[3]):
            img[corner_y + 1][corner_x + 1] = 255; 
            img[corner_y + 0][corner_x + 0] = 255; 
        if(arr[4]):
            img[corner_y + 2][corner_x + 1] = 255; 
            img[corner_y + 2][corner_x + 0] = 255; 
        if(arr[5]):
            img[corner_y + 3][corner_x + 1] = 255; 
            img[corner_y + 4][corner_x + 0] = 255; 
        if(arr[6]):
            img[corner_y + 3][corner_x + 2] = 255; 
            img[corner_y + 4][corner_x + 2] = 255; 
        if(arr[7]):
            img[corner_y + 3][corner_x + 3] = 255; 
            img[corner_y + 4][corner_x + 4] = 255; 

plt.savefig("snowflake.pdf", bbox_inches = 'tight'); 
plt.axis("off"); 
plt.imshow(img);
plt.savefig("snowflake.pdf");  
plt.show(); 

