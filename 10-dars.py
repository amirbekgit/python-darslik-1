#amaliyot

import turtle as t
import turtle
import colorsys
import math
from turtle import *

t.bgcolor("black")
t.tracer(100)
t.pensize(1)
h = 0.5
for i in range(250):
        h = 0.0008
        t.fillcolor("aqua")
        t.begin_fill()
        t.fd(i)
        t.lt(100)
        t.circle(30)
        for j in range(2):
            t.fd(i*j)
            t.rt(109)
        t.end_fill()