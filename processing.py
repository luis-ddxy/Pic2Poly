import cv2 as cv; 
import numpy as np; 
from matplotlib import pyplot as plt; 


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
img2 = cv.Canny(img, 50, 100); 
print(img2[500][0:]); 

# plt.imshow(img2); 
# plt.show()
cv.imshow("image", img2); 
cv.waitKey(0);
cv.destroyAllWindows();  

