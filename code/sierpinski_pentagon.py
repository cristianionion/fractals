from Gkit import *
import math
import random

swidth = 800
sheight = 800

G_init_graphics(swidth, sheight)
G_rgb(0,0,0)
G_clear()

def translate(dx,dy,x,y):
    x +=dx
    y +=dy

    return x,y

def scale(sx,sy,x,y):
    x *=sx
    y *=sy

    return x,y

def rotate(theta,x,y):
    rad = math.radians(theta)
    c = math.cos(rad)
    s = math.sin(rad)

    t = c*x - s*y
    y = s*x + c*y
    x = t

    return x,y



points = []
theta = 90
radius = 0.3

for i in range(5):
    
    px = 0.5 + radius*math.cos(math.radians(theta))
    py = 0.5 + radius*math.sin(math.radians(theta))

    px /= 2.5
    py /= 2.5

    points.append([px,py])

    theta += 72
    

print(points)


p1 = []
p2 = []
p3 = []
p4 = []
p5 = []

def pentagon(r,x,y,i):



    # scaler s
    s = 0.45

    # 5 rules
    if r > 0.8:
        G_rgb(0.6, 0.8, 1.0)
        x, y = scale(s, s, x, y)
        x, y = translate(points[0][0], points[0][1], x, y)
        if i >200:
            p1.append([x * swidth+109, y * sheight+93])

    elif r > 0.6:
        G_rgb(0.8, 0.7, 1.0)
        x, y = scale(s, s, x, y)
        x, y = translate(points[1][0], points[1][1], x, y)
        if i >200:
            p2.append([x * swidth+109, y * sheight+93])

    elif r > 0.4:
        G_rgb(0.75, 0.8, 1.0)
        x, y = scale(s, s, x, y)
        x, y = translate(points[2][0], points[2][1], x, y)
        if i >200:
            p3.append([x * swidth+109, y * sheight+93])

    elif r > 0.2:
        G_rgb(0.85, 0.8, 0.9)
        x, y = scale(s, s, x, y)
        x, y = translate(points[3][0], points[3][1], x, y)
        if i >200:
            p4.append([x * swidth+109, y * sheight+93])

    else:
        G_rgb(0.75, 0.9, 0.85)
        x, y = scale(s, s, x, y)
        x, y = translate(points[4][0], points[4][1], x, y)
        if i >200:
            p5.append([x * swidth+109, y * sheight+93])

    return x, y



xys = []
def draw():
    global x,y
    x = 0.0
    y = 0.0

    G_rgb(0.4,0.7,0.4)

    for i in range(30000):
        r = random.uniform(0,1)

        x,y = pentagon(r,x,y,i)

        xys.append([x*swidth+109,y*sheight+93])

        if i >200: # get rid of some outliers
            G_point(x*swidth+109,y*sheight+93)

draw()



# start with moving one section

G_wait_key()

G_rgb(0,0,0)
G_clear()



# p1
minp1x = maxp1x = p1[0][0]
minp1y = maxp1y = p1[0][1]
minp1xi = maxp1xi = 0
minp1yi = maxp1yi = 0

for i in range(len(p1)):
    x, y = p1[i]

    if x < minp1x:
        minp1x = x
        minp1xi = i
    if x > maxp1x:
        maxp1x = x
        maxp1xi = i
    if y < minp1y:
        minp1y = y
        minp1yi = i
    if y > maxp1y:
        maxp1y = y
        maxp1yi = i


minp2x = maxp2x = p2[0][0]
minp2y = maxp2y = p2[0][1]
minp2xi = maxp2xi = 0
minp2yi = maxp2yi = 0

# p2
for i in range(len(p2)):
    x, y = p2[i]
    if x < minp2x:
        minp2x = x
        minp2xi = i
    if x > maxp2x:
        maxp2x = x
        maxp2xi = i
    if y < minp2y:
        minp2y = y
        minp2yi = i
    if y > maxp2y:
        maxp2y = y
        maxp2yi = i

# p3
minp3x = maxp3x = p3[0][0]
minp3y = maxp3y = p3[0][1]
minp3xi = maxp3xi = 0
minp3yi = maxp3yi = 0

for i in range(len(p3)):
    x, y = p3[i]
    if x < minp3x:
        minp3x = x
        minp3xi = i
    if x > maxp3x:
        maxp3x = x
        maxp3xi = i
    if y < minp3y:
        minp3y = y
        minp3yi = i
    if y > maxp3y:
        maxp3y = y
        maxp3yi = i

# p4
minp4x = maxp4x = p4[0][0]
minp4y = maxp4y = p4[0][1]
minp4xi = maxp4xi = 0
minp4yi = maxp4yi = 0

for i in range(len(p4)):
    x, y = p4[i]
    if x < minp4x:
        minp4x = x
        minp4xi = i
    if x > maxp4x:
        maxp4x = x
        maxp4xi = i
    if y < minp4y:
        minp4y = y
        minp4yi = i
    if y > maxp4y:
        maxp4y = y
        maxp4yi = i

# p5
minp5x = maxp5x = p5[0][0]
minp5y = maxp5y = p5[0][1]
minp5xi = maxp5xi = 0
minp5yi = maxp5yi = 0

for i in range(len(p5)):
    x, y = p5[i]
    if x < minp5x:
        minp5x = x
        minp5xi = i
    if x > maxp5x:
        maxp5x = x
        maxp5xi = i
    if y < minp5y:
        minp5y = y
        minp5yi = i
    if y > maxp5y:
        maxp5y = y
        maxp5yi = i

"""
dx1 = 0.63
dy1 = 0.87
dx2 = 0.49
dy2 = 0.71
dx3 = 0.91
dy3 = 0.34
dx4 = 0.79
dy4 = 0.58
dx5 = 0.22
dy5 = 0.96
"""

dx1 = random.choice([-1, 1]) * random.randint(5, 25)
dy1 = random.choice([-1, 1]) * random.randint(5, 25)
dx2 = random.choice([-1, 1]) * random.randint(5, 25)
dy2 = random.choice([-1, 1]) * random.randint(5, 25)
dx3 = random.choice([-1, 1]) * random.randint(5, 25)
dy3 = random.choice([-1, 1]) * random.randint(5, 25)
dx4 = random.choice([-1, 1]) * random.randint(5, 25)
dy4 = random.choice([-1, 1]) * random.randint(5, 25)
dx5 = random.choice([-1, 1]) * random.randint(5, 25)
dy5 = random.choice([-1, 1]) * random.randint(5, 25)

pbool = [False, False, False, False]

boolcount = 0

print("center x value of polygon: ",p1[maxp1yi])
print("total height of polygon: ",p3[minp3yi][1]-p1[maxp1yi][1])
print("height from bottom: ", p3[minp3yi][1])
while True:

    G_rgb(0,0,0)
    G_clear()
    G_rgb(0.6, 0.8, 1.0)

    if p1[minp1xi][0] < 0 or p1[maxp1xi][0] > swidth :
        dx1 = -dx1

    if p1[minp1yi][1] < 0 or p1[maxp1yi][1] > sheight:
        dy1 = -dy1

    p1 = [[x+dx1, y+dy1] for x, y in p1]

    if pbool[0]:
        if p2[minp2xi][0] < 0 or p2[maxp2xi][0] > swidth:
            dx2 = -dx2
        if p2[minp2yi][1] < 0 or p2[maxp2yi][1] > sheight:
            dy2 = -dy2

        p2 = [[x+dx2, y+dy2] for x, y in p2]
    
    if pbool[1]:
        if p3[minp3xi][0] < 0 or p3[maxp3xi][0] > swidth:
            dx3 = -dx3
        if p3[minp3yi][1] < 0 or p3[maxp3yi][1] > sheight:
            dy3 = -dy3
    
        p3 = [[x+dx3, y+dy3] for x, y in p3]
    
    if pbool[2]:
        if p4[minp4xi][0] < 0 or p4[maxp4xi][0] > swidth:
            dx4 = -dx4
        if p4[minp4yi][1] < 0 or p4[maxp4yi][1] > sheight:
            dy4 = -dy4

        p4 = [[x+dx4, y+dy4] for x, y in p4]

    if pbool[3]:
        if p5[minp5xi][0] < 0 or p5[maxp5xi][0] > swidth:
            dx5 = -dx5
        if p5[minp5yi][1] < 0 or p5[maxp5yi][1] > sheight:
            dy5 = -dy5
    
        p5 = [[x+dx5, y+dy5] for x, y in p5]

    for i in range(len(p1)):
        G_rgb(0.6, 0.8, 1.0)
        G_point(p1[i][0], p1[i][1])
    
    for i in range(len(p2)):
        G_rgb(0.8, 0.7, 1.0)
        G_point(p2[i][0], p2[i][1])
    
    for i in range(len(p3)):
        G_rgb(0.75, 0.8, 1.0)
        G_point(p3[i][0], p3[i][1])
    
    for i in range(len(p4)):
        G_rgb(0.85, 0.8, 0.9)
        G_point(p4[i][0], p4[i][1])
    
    for i in range(len(p5)):
        G_rgb(0.75, 0.9, 0.85)
        G_point(p5[i][0], p5[i][1])


    G_display_image()

    key = G_no_wait_key()
    if key == 'q':
        break
    elif key > 0:
        pbool[boolcount] =  True

        boolcount += 1


    #time.sleep(0.0001)
    




xys.sort()
#print(xys[-200:])
G_rgb(1,1,1)


G_wait_key()