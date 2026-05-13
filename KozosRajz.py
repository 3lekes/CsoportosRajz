#Udud Mátyás - lámpaizzók
#Elekes David - lampatest
#Dóczy Barnabás lámpatalp


import turtle
turtle.speed(11)

#Talp:
turtle.teleport(-25,0)
turtle.color("grey")
turtle.fillcolor("grey")
turtle.begin_fill()
k=0
while k<2:
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    k+=1
turtle.end_fill()



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