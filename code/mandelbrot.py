from ctypes import *
from Gkit import *
import math
import cmath
import time
  
swidth = 800
sheight = 800

G_init_graphics (swidth,sheight) 


G_rgb (0.8, 0.8, 0.8) 
G_clear ()


# complex # is: complex = complex(a,i)



# go through each point on graph: 2 for loops
# set a,b = x,y
#     c = a+b*I
# for loop to see if it converges


ks = []

for i in range(swidth):
    for j in range(sheight):

        x = (i) / 200
        x -= 2 
        y = (j) / 200
        y -= 2 

        c = complex(x,y)

        z = complex(0,0)
        
        for k in range(200):

            z = z**2 + c

            if abs(z) > 2:
                
                
                ks.append(k)
                G_rgb(k*0.8/255,k/255, 240/255)
            
                
                break

        if abs(z) <= 2:
            G_rgb(0,0,0)
            #print(abs(z))

        G_point(i,j)




G_wait_key()