import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for the square
square_turtle = turtle.Turtle()
square_turtle.hideturtle()
square_turtle.penup()
square_turtle.goto(-150, 150)  # Move to top-left corner
square_turtle.pendown()
square_turtle.fillcolor("green")
square_turtle.begin_fill()
for _ in range(4):
    square_turtle.forward(300)  # Make the square larger (300 units per side)
    square_turtle.right(90)
square_turtle.end_fill()

# Create a list of turtles for the circular positions inside the square
turtles = []
side_length = 300  # Length of each side of the square
radius = side_length / 2  # distance turtle center
num_turtles = 12  # Number of tur
# outer turtle thing thingy
for i in range(num_turtles):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("blue")
    # Calculate the angle for each turtle in a circular arrangement (30 degrees apart)
    angle = i * (360 / num_turtles)
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    t.penup()
    t.goto(x, y)
    t.setheading(180 + angle)
    t.forward(15)
    t.pendown()
    t.forward(45)
    t.setheading(180+angle)
    t.penup()
    t.goto(x, y)
    # turtule look outside
    t.setheading(angle + 360)
    turtles.append(t)
# Middle turturll
center_turtle = turtle.Turtle()
center_turtle.shape("turtle")
center_turtle.color("blue")
center_turtle.penup()
center_turtle.goto(0, 0)  # Middle of greeeeennnnnnn
  

square_turtle.hideturtle()
turtle.done()
