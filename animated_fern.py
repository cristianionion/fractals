from ctypes import *
from Gkit import *
import math
import time
  

# https://paulbourke.net/fractals/fracintro/ 
# rules source ^


swidth = 800
sheight = 800

G_init_graphics(swidth, sheight) 

G_rgb(0.8, 0.8, 0.8) 
G_clear()


class Stick():

    def __init__(self, parent, parent_index, parent_pos, angle, dist): 
        self.parent = parent
        self.parent_index = parent_index
        self.x0 = parent_pos[0]
        self.y0 = parent_pos[1]
        self.x1 = self.x0 + dist * math.cos(math.radians(angle))
        self.y1 = self.y0 + dist * math.sin(math.radians(angle))
        self.curr_angle = angle
        self.orig_angle = angle
        self.dist = dist


rules = {
    '.axiom': 'F',
    'F': 'FF+[+F-F-F]-[-F+F+F]',
    '[': '[',
    ']': ']',
    '+': '+',
    '-': '-',
}


branches = []

def bush(depth):
    production = rules['.axiom']
    for i in range(depth):
        c = ''
        for j in production:
            c += rules[j]
        production = c

    angle = 30.0
    theta = 22.5
    turtle = [origin[0],origin[1]]
    dist = 8

    stack = []
    angle_stack = []
    stick_stack = []
    index_stack = []

    curr_stick = None
    curr_index = -1    

    G_rgb(0.4, 0.7, 0.6)
    for i in range(len(production)):
        symbol = production[i]

        if symbol == "F":
            new_x = turtle[0] + dist * math.cos(math.radians(angle))
            new_y = turtle[1] + dist * math.sin(math.radians(angle))

            stick = Stick(curr_stick, curr_index, (turtle[0], turtle[1]), angle, dist)
            branches.append(stick)
            curr_index = len(branches) - 1
            curr_stick = stick

            G_line(turtle[0], turtle[1], new_x, new_y)
            turtle[0] = new_x
            turtle[1] = new_y

        elif symbol == "+":
            angle += theta

        elif symbol == "-":
            angle -= theta

        elif symbol == "[":
            angle_stack.append(angle)
            stack.append(turtle[0])
            stack.append(turtle[1])
            stick_stack.append(curr_stick)
            index_stack.append(curr_index)

        elif symbol == "]":
            turtle[1] = stack.pop()
            turtle[0] = stack.pop()
            angle = angle_stack.pop()
            curr_stick = stick_stack.pop()
            curr_index = index_stack.pop()


def animate(n):
    t = True
    curr = 0
    sway_speed = 0.05
    sway_size = 7.5

    while t:
        G_rgb(0, 0, 0)
        G_clear()

        for i in range(len(branches)):
            stick = branches[i]
            offset = i * 0.15
            sway = math.sin(curr * sway_speed + offset) * sway_size
            stick.curr_angle = stick.orig_angle + sway

        for i in range(len(branches)):
            stick = branches[i]

            if stick.parent is not None:
                base_x = stick.parent.x1
                base_y = stick.parent.y1
            else:
                base_x = origin[0]
                base_y = origin[1]

            stick.x0 = base_x
            stick.y0 = base_y

            stick.x1 = base_x + stick.dist * math.cos(math.radians(stick.curr_angle))
            stick.y1 = base_y + stick.dist * math.sin(math.radians(stick.curr_angle))

            # color stuff
            
            # sine to normalize, /2 to keep within [0,1]
            hue = (math.sin(curr * 0.02 + i * 0.1) + 1) / 2  
            r = 0.5 + 0.5 * hue
            
            # keeping r=g=b gives cool white/grayscale
            #g = 0.5 + 0.5 * hue
            #b = 0.5 + 0.5 * hue
            
            g = 0.5 + 0.4 * (1 - hue)
            b = 0.6 + 0.3 * math.sin(hue * math.pi)
            G_rgb(r, g, b)

            #G_rgb(0.4, 0.8, 0.7)
            G_line(stick.x0, stick.y0, stick.x1, stick.y1)

        G_display_image()
        time.sleep(1/60.0)
        curr += 1

    
origin = (10.0,10.0)

print("Enter depth (try 4 or 5): ")

# looks sick with dist = 8, n = 5 (slow tho)
# messing with curr incrementation and sway_size gives cool outcomes
n = int(input())
bush(n)
animate(n)

G_wait_key()
