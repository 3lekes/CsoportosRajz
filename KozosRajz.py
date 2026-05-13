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
    turtle.setheading(0)
    turtle.fillcolor(colors[i%3])
    turtle.color(colors[i%3])
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(125)
    turtle.pendown()
    i+=1

turtle.done()