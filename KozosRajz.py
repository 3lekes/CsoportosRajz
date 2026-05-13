#Udud Mátyás - lámpaizzók
#Elekes David - lampatest
#Dóczy Barnabás lámpatalp

import turtle
turtle.speed(11)

#Talp:

#Test:
turtle.teleport(-62.5, -25)
turtle.color("black")
turtle.fillcolor("black")
turtle.begin_fill()
j=0
while j<2:
    turtle.forward(125)
    turtle.left(90)
    turtle.forward(323)
    turtle.left(90)
    j+=1
turtle.end_fill()

#Izzok:
turtle.teleport(0,0)
colors=["green", "yellow", "red"]
i=0
while i<3:
    turtle.setheading(0)
    turtle.fillcolor(colors[i%3])
    turtle.color(colors[i%3])
    turtle.begin_fill()
    turtle.circle(35)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(100)
    turtle.pendown()
    i+=1

turtle.done()