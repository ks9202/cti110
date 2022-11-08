import turtle
win = turtle.Screen()
samJr = turtle.Turtle()

# Initialize count
count = 0
# Initial display options
win.bgcolor("#F6D0E2")
samJr.pensize(3)
samJr.pencolor("#D53D69")
samJr.shape("turtle")

# Position for letter K
samJr.penup()
samJr.setpos(-250.00,0.00)
samJr.left(90)
# Draw K
samJr.pendown()
samJr.forward(150)
samJr.right(180)
samJr.forward(75)
samJr.left(135)
samJr.forward(100)
samJr.right(180)
samJr.forward(100)
samJr.left(90)
samJr.forward(100)
samJr.penup()

# Position and display options for letter J
samJr.left(135)
samJr.forward(140)
samJr.right(90)
samJr.forward(30)
win.bgcolor("#F2ECEB")
samJr.pencolor("#246197")
# Draw J
samJr.pendown()
samJr.forward(100)
samJr.left(180)
samJr.forward(50)
samJr.left(90)
samJr.forward(120)
samJr.right(45)
samJr.forward(30)
samJr.right(45)
samJr.forward(30)
samJr.penup()

# Reset count
count = 0

# Position and display options for letter S
samJr.right(90)
samJr.forward(140)
samJr.right(90)
samJr.forward(220)
samJr.right(180)
win.bgcolor("#FED6C0")
samJr.pencolor("#E36A25")
# Draw S
samJr.pendown()
samJr.forward(50)
while count < 18:
    samJr.forward(5)
    samJr.left(10)
    count += 1
count = 0
while count < 9:
    samJr.forward(15)
    samJr.right(20)
    count += 1
samJr.forward(40)
samJr.penup()

# Make Sam Jr. spin
samJr.right(90)
samJr.forward(70)
samJr.right(90)
samJr.forward(150)
count = 0
while count < 30:
    samJr.right(90)
    count += 1

win.mainloop()
