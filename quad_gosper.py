from ctypes import *
from Gkit import *
import math
import time


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



def quad_gos(depth): # works well with depth < 12

    # build string
    production = rules['.axiom']

    
    for i in range(depth):


        c = ''

        for j in production:

            c += rules[j]

        production = c

        #print(production)

    
    # interpret string

    # start angle
    angle = 0.0
    # theta to be changed
    theta = 90.0
    turtle = [10.0, 790.0]
    dist = 6.3
    

    stack = []
    angle_stack = []

    #print(production)

    

    G_rgb(0.4,0.7,0.6)
    
    for i in range(len(production)):


        if production[i] == "F":

            new_x = turtle[0] + dist * math.cos(math.radians(angle))
            new_y = turtle[1] + dist * math.sin(math.radians(angle))
            G_line(turtle[0], turtle[1], new_x, new_y)
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

    

       
points = [[10,790]]


print("enter depth (looks good w 3): ")
n = int(input())
quad_gos(n)



G_wait_key()
