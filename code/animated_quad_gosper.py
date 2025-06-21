from ctypes import *
from Gkit import *
import math
import time
import random


# https://paulbourke.net/fractals/lsys/
# quadratic gosper - Dekking

swidth = 800
sheight = 800

G_init_graphics (swidth,sheight) 


G_rgb (0,0,0) 
G_clear ()

# tree
# https://graphicmaths.com/fractals/l-systems/l-system-trees/
# rules
# F: G[+F]-F
# G: GG
rules = {
    '.axiom': '-YF',
    'F': 'F',
    'X': 'XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-',
    'Y': '+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY',
    '[': '[',
    ']': ']',
    '+': '+',
    '-': '-',
}

# it. 1: G+[[F]-F]-G[-GF]+F
# it. 2: GG+[[G+[[F]-F]-G[-GF]+F]-G+[[F]-F]-G[-GF]+F]- GG[-GGG+[[F]-F]-G[-GF]+F]+G+[[F]-F]-G[-GF]+F



def quad_gos(depth): 

    # build string
    production = rules['.axiom']

    
    for i in range(depth):


        c = ''

        for j in production:

            c += rules[j]

        production = c

        print(production)

    
    # interpret string

    # start angle
    angle = 0.0
    # theta to be changed
    theta = 90.0
    turtle = [25.0, 775.0]
    dist = 30
    

    stack = []
    angle_stack = []

    #print(production)

    

    G_rgb(0.4,0.7,0.6)
    
    for i in range(len(production)):


        if production[i] == "F":

            new_x = turtle[0] + dist * math.cos(math.radians(angle))
            new_y = turtle[1] + dist * math.sin(math.radians(angle))
            #G_line(turtle[0], turtle[1], new_x, new_y)
            turtle[0] = new_x
            turtle[1] = new_y

            points.append([turtle[0],turtle[1]])
        
        if production[i] == "+":
            angle += theta
        
        if production[i] == "-":
            angle -= theta

        # store curr loc
        if production[i] == '[':
            #angle_stack = [angle] + angle_stack
            #stack = [turtle[0],turtle[1]] + stack
            angle_stack.append(angle)
            stack.append(turtle[0])
            stack.append(turtle[1])
            #print("stack: ", stack)

        
        # pop removes last element, list can be a stack but backwards
        if production[i] == ']':
            turtle[1] = stack.pop()
            turtle[0] = stack.pop()
            angle = angle_stack.pop()
            #print('pop: ', turtle)
            #print("stack: ", stack)

    

       
points = [[25,775]]


print("enter depth (looks good w 2): ")
n = int(input())
quad_gos(n)

for i in range(len(points)-1):
    G_display_image()
    # place point at each spot, change color incrementally
    midx = (points[i][0] + points[i+1][0]) / 2
    midy = (points[i][1] + points[i+1][1]) / 2

    
    
    
    # color selection, less vibrant
    r = random.uniform(0.2,0.5)
    g = random.uniform(0.3,0.4)
    b = random.uniform(0.1,0.5)
    

    G_rgb(r,g,b)
    G_fill_circle(midx, midy, 5)
    
    #G_fill_circle(midx2,midy2, 18)
    

    # wait for time 
    #time.sleep(0.02)


# connect the lines of the fractal after a key press
G_wait_key()

for i in range(len(points)-1):
    
    G_rgb(0.9,0.4,0.9)

    G_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1])


    time.sleep(0.03)

    G_display_image()


i = 0
while True:


    hue = (math.sin(i * 0.12))  

    r = 0.5 + 0.5 * hue
    g = 0.5 + 0.4 * (1 - hue)
    b = 0.6 + 0.3 * math.sin(hue * math.pi)
    G_rgb(r, g, b)
    G_display_image()
    for j in range(len(points)-1):
                

        G_line(points[j][0], points[j][1], points[j+1][0], points[j+1][1])



    #G_display_image()

    time.sleep(0.08)
    i += 1
    key = G_no_wait_key()
    if key >0:
        break

    


#quad_gos(n)

G_wait_key()
