from ctypes import *
from Gkit import *
import cmath
import random


swidth = 900
sheight = 900
size = 300  

G_init_graphics(swidth, sheight)
G_rgb(0.0,0.0,0.0)
G_clear()

k_points = []

for i in range(int(swidth/3)):
    for j in range(int(sheight/3)):

        x = (i / 75) - 2
        y = (j / 75) - 2
        
        c = complex(x,y)
        z = complex(0,0)

        for k in range(200):

            z = cmath.cos(z)*cmath.sin(z) + c

            if abs(z) > 2:
                
                
                G_rgb((k+55)/255,(k+55)/255, (k+55)/255)

                # if point is close to edge add to a list

                if k > 5:
                    k_points.append([i,j])
                
                break

        if abs(z) <= 2:
            G_rgb(0,0,0)
            #print(abs(z))

        G_point(i+swidth/3,j+sheight/3)



print(len(k_points))
#print(k_points)


colors = [
    (255,152,59),
    (255,239,45),
    (139,255,45),
    (45,255,178),
    (45,228,255),
    (142,45,255),
    (240,45,255),
    (255,45,103)
]

offsets = [
    [0,600],
    [300,600],
    [600,600],
    [0,300],
    [600,300],
    [0,0],
    [300,0],
    [600,0]
]


# create Julia sets from interesting points from 
t = True
while t:

    exit = [0,0]
    G_wait_click(exit)
    if exit[1] < 300:
        break

    # redraw mandelbrot to cover dots from this sample
    for i in range(int(swidth/3)):
        for j in range(int(sheight/3)):

            x = (i / 75) - 2
            y = (j / 75) - 2
            
            c = complex(x,y)
            z = complex(0,0)

            for k in range(200):

                z = cmath.cos(z)*cmath.sin(z) + c

                if abs(z) > 2:
                    
                    
                    G_rgb((k+55)/255,(k+55)/255, (k+55)/255)

                    # if point is close to edge add to a list
                    break

                if abs(z) <= 2:
                    G_rgb(0,0,0)
                    #print(abs(z))

            G_point(i+swidth/3,j+sheight/3)


    

    chosen = random.sample(k_points,8)

    for n in range(8):

        r = colors[n][0]
        g = colors[n][1]
        b = colors[n][2]

        c = complex(chosen[n][0]/75 - 2,chosen[n][1]/75 - 2)
        
        G_rgb(r/255,g/255,b/255)
        G_fill_circle(chosen[n][0]+300,chosen[n][1]+300,3)

        for i in range(int(swidth/3)):
            for j in range(int(sheight/3)):

                x = (i / 75) - 2
                y = (j / 75) - 2

                z = complex(x,y)
                

                for k in range(200):

                    try:
                        z = cmath.cos(z)*cmath.sin(z) + c
                    except:
                        break

                    if abs(z) > 100:
                        
                        G_rgb(r/255,g/255, b/255)
                        break

                    
                if abs(z.real) <= 1e6 and abs(z.imag) <= 1e6:
                    G_rgb(0,0,0)


                x_offset = offsets[n][0]
                y_offset = offsets[n][1]

                G_point(i+x_offset,j+y_offset)


    

#G_wait_key()

