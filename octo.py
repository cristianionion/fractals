from ctypes import *
from Gkit import *
import math
import random
  
swidth = 800
sheight = 800

G_init_graphics (swidth,sheight) 


G_rgb (0, 0, 0) 
G_clear ()

# background color
# gonna go from lighter blue to darker blue

greens = [15/255,49/255]
blues = [95/255,1.0]

for i in range(sheight):
    G_rgb(0.0, greens[0] + (greens[1]-greens[0])*(i/sheight), blues[0] + (blues[1]-blues[0])*(i/sheight))
    G_line(0,i,swidth,i)

# fish 

def fish(x0,y0):

    # tail
    tail_len = random.randint(20,45)
    tail_height = tail_len*.45
    tail_x = [0, tail_len, 0]
    tail_y = [0, tail_height, tail_height*2]
    for i in range(len(tail_x)):
        tail_x[i] += x0
        tail_y[i] += y0

    body_size = tail_len*.5



    # draw the fish
    red = random.randint(100,255)/255
    green = random.randint(100,255)/255
    blue = random.randint(100,255)/255
    fish_color = (red, green, blue)
    G_rgb(red, green, blue)

    
    G_fill_polygon(tail_x, tail_y)
    G_fill_circle(x0+tail_len*0.85,y0+tail_height, body_size)

    # eyes
    G_rgb(0.0, 0.0, 0.0)
    G_fill_circle(x0+tail_len*1.15,y0+tail_height*1.2, body_size*0.2)
    G_rgb(1.0, 1.0, 1.0)
    G_fill_circle(x0+tail_len*1.15,y0+tail_height*1.2, body_size*0.1)

    fishs.append((x0,y0,tail_x, tail_y, tail_len, tail_height, body_size, fish_color))


fishs = []

# randomly place the fish, somewhat even spacing
for i in range(6):
    for j in range(6):
        x = random.uniform(i*swidth/6, (i+1)*swidth/6)
        y = random.uniform(j*sheight/6, (j+1)*sheight/6)
        fish(x,y)



# pythagoras tree (octopus)
# center is an octagon
# each edge gets a triangle going outward
# one edge of each triangle gets a square going outward
# repeat pythagoras tree for each square
# result should look like a an octopus with spiraling arms

# input to this should be the edge a triangle and rectangle that should
#       be build onto
def octopus(x0, y0, length, angle, depth,t, tri_color, sqr_color):
    
    # rotate
    rot_mx = [[math.cos(math.radians(angle)),-1.0* math.sin(math.radians(angle))],
              [math.sin(math.radians(angle)),      math.cos(math.radians(angle))]]
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
    if depth > 0:
        G_rgb(sqr_color[0],sqr_color[1],sqr_color[2])
        
        left_len = math.sqrt(abs((length*t)**2 + (length*t)**2))
        #left_x = [0.0,left_len,left_len,0.0]
        #left_y = [0.0,0.0,left_len*3,left_len*3]

        left_x = [0.0,left_len,left_len,0.0]
        left_y = [0.0,0.0,left_len*3.5,left_len*3.5]


        # rotate

        left_theta = math.asin((length*t)/left_len)
        left_theta += math.radians(angle)
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


    if depth > 0:
        octopus(left_x[3], left_y[3], left_len, math.degrees(left_theta), depth-1, t, tri_color, sqr_color)

    pass

print("enter depth level (looks good w 4+): ")

n = int(input())

# initial octagon

x = []
y = []

# draw polygon starting bottom left going counter clockwise
theta = 247.5
# side length
length = 60.0
# angle at center of octagon is 22.5, using sin = o/h by splitting the triangle in half
# sin(22.5) = 25 / r
# r = 25 / sin(22.5)

radius = length*0.5 / math.sin(math.radians(22.5))

for i in range(8):
    x.append(399+radius * math.cos(math.radians(theta)))
    y.append(399+radius * math.sin(math.radians(theta)))
    theta += 45.0

# draw octagon
#G_rgb(0.5,0.3,0.4)

# 142, 47, 159
G_rgb(142/255, 47/255, 159/255)

G_fill_polygon(x, y)

# draw smile
G_rgb(1.0, 1.0, 1.0)
G_fill_circle(swidth/2, sheight/2 -20, 30)
G_rgb(142/255, 47/255, 159/255)
G_fill_circle(swidth/2, sheight/2 -18, 30)

# give octo eyes

G_rgb(0.0, 0.0, 0.0)
G_fill_circle(swidth/2 - 30, sheight/2 + 20, 18)
G_fill_circle(swidth/2 + 32, sheight/2 + 18, 18)
G_rgb(1.0, 1.0, 1.0)
G_fill_circle(swidth/2 - 30, sheight/2 + 20, 12)
G_fill_circle(swidth/2 + 32, sheight/2 + 18, 12)

tri_color = (0.8,0.3,0.8)
sqr_color = (0.7,0.45,0.75)

# draw the tree to the depth of n

for i in range(8):
    octopus(x[i], y[i], length, 135.0 + i*45.0, n, 0.61, tri_color, sqr_color)




#G_save_image_to_file("octo.xwd")

#fname = "octo.bmp"
#G_save_to_bmp_file(fname)


G_wait_key()
