from turtle import *

speed(30)
width(7)
color('purple')
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
color("yellow")
begin_fill()
left(90)

forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

penup()
goto(145,100)
pendown()

color("yellow")
begin_fill()
left(120)
forward(40)

left(90)
forward(55)

left(90)
forward(40)

left(90)
forward(55)

penup()
goto(15,100)
pendown()

left(90)
forward(40)
left(90)
forward(55)
left(90)
forward(40)
left(90)
forward(55)
end_fill()

penup()
goto(0,0)
pendown()
color("purple")
left(90)
forward(200)

exitonclick()