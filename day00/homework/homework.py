from turtle import *

#we want to paint a house 

#step 1: draw a square

speed(10)

width(7)
color("brown")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door


begin_fill()
forward(75)
color("yellow")
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)

end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw the windows

#step 1:build a 2 little square inside square one left one right inverted 

penup()
goto(140,140)
pendown()

color("blue")

begin_fill()

left(120)
forward(40)

left(90)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

penup()
goto(15,140)
pendown()

left(90)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

left(90)
forward(45)

end_fill()

exitonclick()