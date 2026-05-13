#Udud Mátyás - lámpaizzók
#Elekes David - lampatest
#Dóczy Barnabás lámpatalp

import turtle

#Talp:

#Test:

#Izzok:
turtle.teleport(0,0)
colors=["green", "yellow", "red"]
i=0
while i<3:
    turtle.fillcolor(colors[i%3])
    turtle.color(colors[i%3])
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(150)
    turtle.pendown()
