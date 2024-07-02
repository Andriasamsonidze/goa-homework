from turtle import *
#we want to paint a house

#step 1 draw a square

speed(10)
width(7)
color("red")
forward (200)
left(90)

forward(200)
left(90)

forward (200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("black")
left(90)
forward(100)   #height of the door
right(90)
forward(60)
right(90)
forward(100)

penup()
goto(200, 200)
pendown()


color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#making windows
color("red")
left(30)
forward(25)

color("black")
right(-90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)

color("red")
forward(20)
right(90)
forward(200)
right(90)
forward(25)

color("black")
right(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)




exitonclick()