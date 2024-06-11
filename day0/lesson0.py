from turtle import *

speed(10)

#we want to paint a house

#step 1: draw a square

begin_fill()

width(5)
color("orange")
forward(200) #length of the cube
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#end of drawing a cube

#drawing a door
begin_fill()

forward(70)
left(90)

color("black")

forward(100) #height of the door
right(90)

forward(50) #length of the door
right(90)

forward(100)
end_fill()

#end of drawing a door

#drawing a roof

color("brown")
penup()
goto(200, 200)
pendown()

begin_fill()

right(150)
forward(200)

left(120)
forward(200)

end_fill()


#end of drawing a roof

#drawing windows

begin_fill()

color("cyan")

penup()
goto(200, 200)
pendown()

left(30)
forward(70)

right(90)
forward(60)

right(90)
forward(70)

right(90)
forward(60)

right(90)
right(90)

penup()

forward(200)

pendown()

right(90)
right(90)

forward(70)

right(90)
forward(70)

right(90)
forward(70)

#end of drawing a house :D



end_fill()
