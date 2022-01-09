#! python

from canvas import Canvas
from shapes import Square,Rectangle
from random import randint

canvas = Canvas(width=600, height=400, color=(255, 255, 255))
rectangle1 = Rectangle(x=randint(0,100), y=randint(0,100), width=randint(100,200), height=randint(100,200), color=(0,132,255))
rectangle1.draw(canvas)
rectangle2 = Rectangle(x=randint(100,250), y=randint(300,400), width=randint(100,200), height=randint(50,100), color=(255,132,132))
rectangle2.draw(canvas)
square1 = Square(x=randint(100,250), y=randint(100,250), side=randint(50,150), color=(132,255,0))
square1.draw(canvas)
canvas.make("canvas.png")