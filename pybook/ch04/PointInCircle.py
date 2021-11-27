import turtle

x1, y1 = eval(input("Enter the center of a circle x, y: "))
radius = eval(input("Enter the radius of the circle: "))
x2, y2 = eval(input("Enter a point x, y: "))

# Draw the circle
turtle.penup()
turtle.goto(x1, y1 - radius)
turtle.pendown()
turtle.circle(radius)
# Draw the point
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(3)
turtle.end_fill()

# Display the status
turtle.penup()
turtle.goto(x1 - 70, y1 - radius - 20)
turtle.pendown()

d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (x2 - x1)) ** 0.5
if d <= radius:
  turtle.write("The point is inside the circle")
else:
  turtle.write("The point is outside the circle")

turtle.hideturtle()

turtle.done()
