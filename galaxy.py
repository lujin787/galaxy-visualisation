import turtle
import math
import random
screen = turtle.Screen()
screen.setup(600,600)
screen.tracer(0)
screen.bgcolor("#000435")
t=turtle.Turtle()
t.hideturtle()
t.penup()
TILT = 0.55
def glow(h,v=1.0):
    return colorsys.hsv_to_rgb(h%1,0.7,v)

def stars():
    stars_colors = ["#ffa333","#fffbeb","#e0fffb","#09eefc"]
    for i in range(300):
        x=random.randint(-400,400)
        y=random.randint(-300,300)
        t.goto(x,y)
        size = random.choice([1,2,3])
        color = random.choice(stars_colors)
        t.dot(size,color)
def dust():
    colors = ["#2b1954","#4a1c6b","#1b3668"]
    for i in range(400):
        angle = random.uniform(0,2*math.pi)
        dist = random.gauss(140,75)
        x = dist*math.cos(angle)*1.35
        y = dist*math.sin(angle)*0.65
        t.goto(x,y)
        t.dot(random.randint(2,4),random.choice(colors))
def arms(points):
    palette = ["#fff3c4","#ff7eb3","#ff4791","#b537f2","#6b5ce7","#4895ef"]
    for i in range(points):
        progress = i/points
        arm_offset = (i%2)*math.pi
        angle = progress*4.5*math.pi+arm_offset
        radius = progress*260
        spraed = random.gauss(0,progress+11)
        x=(radius+spraed)*math.cos(angle)*1.35
        y=(radius+spraed)*math.sin(angle)*0.65
        color_idx=min(int(progress*len(palette)),len(palette)-1)
        t.goto(x,y)
        t.dot(random.uniform(2,4.5),palette[color_idx])
def core():
    core_color = ["#ffce76","#fff3c4","#ffffff"]
    for i, color in enumerate(core_color):
        for j in range(90-i*15):
            angle=random.uniform(0,2*math.pi)
            dist=random.uniform(0,32-i*6)
            x=dist*math.cos(angle)*1.3
            y=dist*math.sin(angle)*0.7
            t.goto(x,y)
            t.dot(random.uniform(3,6),color)
def sparkles():
    for i in range(60):
        angle = random.uniform(0,2*math.pi)
        dist = random.uniform(10,120)
        x = dist*math.cos(angle)*1.35
        y = dist*math.sin(angle)*0.65
        t.dot(random.uniform(5,10),"#ffffff")
sparkles()
core()
arms(2000)        
dust()
stars()
turtle.done()
