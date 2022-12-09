import numpy as np; 
import math as mt; 

num_splines = 10; 

x_values = np.linspace(0, 2, num = num_splines * 2 + 1); 

for i in range(0, num_splines):
    x_sub = x_values[2 * i : 2 * (i+1) + 1]; 

    x_entry = np.ones((3,3)) * x_sub; 
    x_entry = x_entry.transpose(); 
    x_entry = np.power(x_entry, [2, 1, 0]); 

    y_entry = np.sqrt(1 - np.square(x_sub - 1)); 

    poly = np.linalg.solve(x_entry, y_entry); 

    #print(x_sub); 
    #print(poly); 

    print("y = ", poly[0], "x^2 + ", poly[1], "x + ", poly[2], "\left\{", x_sub[0], "<= x <=", x_sub[2], r"\right\}"); 



#print(xEntry); 


def upper_circle(x, a = 0, b = 0, r = 1):
    return mt.sqrt(r**2 - (x-a)**2) + b; 
