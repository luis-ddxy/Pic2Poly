import cv2 as cv; 
import numpy as np; 
from matplotlib import pyplot as plt; 
import time; 

img = cv.imread("test4.png"); 
img = cv.GaussianBlur(img, (5,5), sigmaX=5, sigmaY=5)

edges = cv.Canny(img, 50, 100); 
edgesBool = np.where(edges == 255, True, False); 

features = []; 


def active_neighbors(row, col):
    neighbors = []; 
    active = []; 

    if row > 0:
        neighbors.append(["up", row - 1, col]); 
        if col < edges.shape[1] - 1: 
            neighbors.append(["rightUp", row - 1, col + 1]); 
        if col > 0: 
            neighbors.append(["leftUp", row - 1, col - 1]); 
    
    if row < edges.shape[0] - 1:
        neighbors.append(["down", row + 1, col]); 
        if col < edges.shape[1] - 1:
            neighbors.append(["rightDown", row + 1, col + 1]); 
        if col > 0:
            neighbors.append(["leftDown", row + 1, col - 1]); 
    
    if col < edges.shape[1] - 1:
        neighbors.append(["right", row, col + 1]); 
    if col > 0: 
        neighbors.append(["left", row, col - 1]); 

    for neighbor in neighbors:
        if edgesBool[neighbor[1]][neighbor[2]]:
            active.append(neighbor); 
    
    return active; 

def perpendicular(dir):
    dirs = []; 
    if dir == "right" or dir == "left":
        dirs = ["up", "down"]; 
    elif dir == "up" or dir == "down":
        dirs = ["left", "right"]; 
    elif dir == "rightDown" or dir == "leftUp":
        dirs = ["rightUp", "leftDown"]; 
    elif dir == "rightUp" or dir == "leftDown":
        dirs = ["rightDown", "leftUp"]; 
    return dirs; 

def track_line(row, col, local_dir = "none", global_dir = "none"):
    
    if local_dir == "none":
        features.append([]); 

    features[len(features) - 1].append([row, col]); 
    edgesBool[row][col] = False;  

    neighbors = active_neighbors(row, col); 

    if len(neighbors) == 1:
        if not ((neighbors[0][0] == "right" and global_dir == "left") or
        (neighbors[0][0] == "left" and global_dir == "right")):
            local_dir = neighbors[0][0];
        else:
            # maybe nothing
            pass; 
        
        if global_dir == "none" and (neighbors[0][0] == "left" or neighbors[0][0] == "right"):
            global_dir = neighbors[0][0]
        
        track_line(neighbors[0][1], neighbors[0][2], local_dir, global_dir); 

    elif len(neighbors) > 1 and local_dir != "none":
        can_follow_dir = False; 
        for neighbor in neighbors:
            if neighbor[0] == local_dir:
                can_follow_dir = True; 
                track_line(neighbor[1], neighbor[2], local_dir, global_dir); 
        
        if (not can_follow_dir) and len(neighbors) == 2:
            for neighbor in neighbors:
                if neighbor[0] in perpendicular(local_dir):
                    track_line(neighbor[1], neighbor[2], neighbor[0], global_dir); 
                # if neighbor[0] == "right":
                #     track_line(neighbor[1], neighbor[2], neighbor[0], global_dir); 


# for row in range(edges.shape[0] - 1):
#     for col in range(edges.shape[1] - 1): 
#         if edgesBool[row][col] and edgesBool[row + 1][col] and edgesBool[row][col + 1]:
#             edgesBool[row][col] = False; 
#         elif edgesBool[row][col] and edgesBool[row + 1][col] and col > 0:
#             if edgesBool[row + 1][col - 1]:
#                 edgesBool[row + 1][col] = False; 

for row in range(edges.shape[0] - 1):
    for col in range(edges.shape[1] - 1): 
        if edgesBool[row][col]: 
            neighbors = active_neighbors(row, col); 
            directions = []; 
            for neighbor in neighbors: 
                directions.append(neighbor[0]); 
            
            if (("down" in directions and "rightDown" in directions) or 
            ("down" in directions and "leftDown" in directions)):
                edgesBool[row + 1][col] = False; 
            elif ("right" in directions and "down" in directions): 
                edgesBool[row][col] = False; 

for row in range(edges.shape[0]):
    for col in range(edges.shape[1]): 
        if edgesBool[row][col]:
            track_line(row, col); 

print(len(features)); 

cleanFeat = []; 
cleanImg = np.zeros((edges.shape[0], edges.shape[1])); 

for feat in features:
    if len(feat) > 10: 
        cleanFeat.append(feat); 

for feat in cleanFeat:
    for pixel in feat:
        cleanImg[pixel[0]][pixel[1]] = 255; 

print(len(cleanFeat)); 

plt.subplot(1, 2, 1); 
plt.imshow(edges); 
plt.subplot(1, 2, 2); 
plt.imshow(cleanImg); 
plt.show(); 