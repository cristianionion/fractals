from ctypes import *
from Gkit import *
import math
  
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
    '.axiom': 'F',
    'F': 'G+[[F]-F]-G[-GF]+F',
    'G': 'GG',
    '[': '[',
    ']': ']',
    '+': '+',
    '-': '-',
}

# it. 1: G+[[F]-F]-G[-GF]+F
# it. 2: GG+[[G+[[F]-F]-G[-GF]+F]-G+[[F]-F]-G[-GF]+F]- GG[-GGG+[[F]-F]-G[-GF]+F]+G+[[F]-F]-G[-GF]+F


def branch(depth):

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
    angle = 90.0
    # theta to be changed
    theta = 15.0
    turtle = [399.0, -20.0]
    dist = 10.0
    

    stack = []
    angle_stack = []

    #print(production)

    start = 0
    for i in range(len(production)):
        if production[i] == 'F':
            start = i
            break
    
    #production = production[start:-1]

    #print(start,production)

    G_rgb(0.4,0.7,0.6)
    for i in range(len(production)):


        if production[i] == "F" or production[i] == "G":

            new_x = turtle[0] + dist * math.cos(math.radians(angle))
            new_y = turtle[1] + dist * math.sin(math.radians(angle))
            G_line(turtle[0], turtle[1], new_x, new_y)
            turtle[0] = new_x
            turtle[1] = new_y
        
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



       

print("enter depth (looks best with 4or5): ")
n = int(input())
branch(n)




G_wait_key()
