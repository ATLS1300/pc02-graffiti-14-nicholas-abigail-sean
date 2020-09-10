#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Sean Heckin' Riddle
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = 'Bezos.gif'
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

Turtle()
up()
#mustache 1
goto(23,60) 
left(140)
width(6)
down()
begin_fill()
forward(25)
left(80)
forward(55)
right(205)
forward(67)
left(42)
forward(23)
right(97)
forward(40)
right(147)
forward(47)
end_fill()

#laser eyes
up()
color("red")
goto(40,122)
left(146)
width(3)
down()
forward(750)
up()
goto(-16,111)
right(20)
down()
forward(700)

#lolololol
width(8)
up()
home()
goto(-350,100)
color("black")
right(90)
down()
forward(50)
left(90)
forward(25)
up()
goto(-280,50)
down()
circle(25)
up()
goto(-220,100)
right(90)
down()
forward(50)
left(90)
forward(25)
up()

done()

#this is art

#=======Add your code here======


