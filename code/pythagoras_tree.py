from ctypes import *
from Gkit import *
import math
  
swidth = 800
sheight = 800

G_init_graphics (swidth,sheight) 


G_rgb (0,0,0) 
G_clear ()


n = int(input())

# initial square
sqr_color = (0.2,0.6,0.7)
G_rgb(sqr_color[0],sqr_color[1],sqr_color[2])
x0 = 325.0
y0 = 100.0
x1 = 475.0
y1 = 100.0
x2 = 475.0
y2 = 250.0
x3 = 325.0
y3 = 250.0


x = [x0,x1,x2,x3]
y = [y0,y1,y2,y3]

G_fill_polygon(x,y)


# idea
# store triangle + 2 squares on origin (bottom left of triangle on 0,0)
# scale them to what previous square len was
# rotate them 
# translate them
# then draw,
# so store like: triangle = G_fill_triangle(), left_square = G_fill_polygon(),...
# then after translated, call them?

# just need x0, y0, length, and depth?
# x0,y0 just to know for translation
def pythagoras(x0,y0,length,theta,depth,t, tri_color, sqr_color):

    rot_mx = [[math.cos(math.radians(theta)),-1.0* math.sin(math.radians(theta))],
              [math.sin(math.radians(theta)),      math.cos(math.radians(theta))]]
    
    
    tri_x = [0.0,length,length*t]
    tri_y = [0.0,0.0,length*t]

    # rotate 
    for i in range(len(tri_x)):
        x = tri_x[i]
        y = tri_y[i]
        tri_x[i] = rot_mx[0][0]*x + rot_mx[0][1]*y
        tri_y[i] = rot_mx[1][0]*x + rot_mx[1][1]*y
    
    # translate
    for i in range(len(tri_x)):
        tri_x[i] += x0
        tri_y[i] += y0
    G_rgb(tri_color[0],tri_color[1],tri_color[2])
    G_fill_polygon(tri_x,tri_y)
    

    
    # left square
    G_rgb(sqr_color[0],sqr_color[1],sqr_color[2])
  
    left_len = math.sqrt(abs((length*t)**2 + (length*t)**2))
    left_x = [0.0,left_len,left_len,0.0]
    left_y = [0.0,0.0,left_len,left_len]


    # rotate

    left_theta = math.asin((length*t)/left_len)
    
    left_theta += math.radians(theta)

    left_rot_mx = [[math.cos(left_theta), -math.sin(left_theta)],
                   [math.sin(left_theta),  math.cos(left_theta)]]
    
    for i in range(len(left_x)):
        x = left_x[i]
        y = left_y[i]
        left_x[i] = left_rot_mx[0][0]*x + left_rot_mx[0][1]*y
        left_y[i] = left_rot_mx[1][0]*x + left_rot_mx[1][1]*y

    # translate
    for i in range(len(left_x)):
        left_x[i] += x0
        left_y[i] += y0
    
    G_fill_polygon(left_x,left_y)
    #print(left_x, left_y)


    # right square

    right_len = math.sqrt(abs((length*(1-t))**2 + (length*(t))**2))
    
    right_x = [0.0,right_len,right_len,0.0]
    right_y = [0.0,0.0,right_len,right_len]

    # rotate

    right_theta = -1* math.pi / 2  + math.cos(length*t/right_len)
    right_theta = -1*math.asin((length*(t))/right_len)
    right_theta += math.radians(theta)
    

    
    right_rot_mx = [[math.cos(right_theta),-1.0* math.sin(right_theta)],
                    [math.sin(right_theta),      math.cos(right_theta)]]
    
    for i in range(len(right_x)):
        x = right_x[i]
        y = right_y[i]
        right_x[i] = right_rot_mx[0][0]*x + right_rot_mx[0][1]*y
        right_y[i] = right_rot_mx[1][0]*x + right_rot_mx[1][1]*y

    # translate
    for i in range(len(right_x)):
        right_x[i] += tri_x[2]
        right_y[i] += tri_y[2]


    G_fill_polygon(right_x,right_y)
    

    # try recursion 

    if depth > 0:
        pythagoras(left_x[3],left_y[3],left_len,math.degrees(left_theta),depth-1,t,tri_color,sqr_color)
        pythagoras(right_x[3],right_y[3],right_len,math.degrees(right_theta),depth-1,t,tri_color,sqr_color)



pythagoras(x3,y3,abs(x1-x0),0.0,n,0.5, (0.9,0.4,0.3),sqr_color)

G_wait_key()