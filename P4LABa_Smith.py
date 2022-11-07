import turtle
win = turtle.Screen()
sam = turtle.Turtle()

# Initial display options, initialize count
win.bgcolor("#E2E8FD")
sam.pensize(2)
sam.pencolor("#2F49A3")
sam.shape("turtle")
count = 0

# Position for triangle
sam.penup()
sam.setpos(-250.00,-50.00)
sam.pendown()
# Draw triangle
while count < 4:
    sam.forward(250)
    sam.left(120)
    count += 1

# Reset count
count = 0

# Position and display options for first square
sam.penup()
sam.setpos(90.00,0.00)
sam.pencolor("#2FA363")
sam.pendown()
# Draw first square
while count < 4:
    sam.forward(200)
    sam.right(90)
    count += 1

# Reset count
count = 0

# Position and display options for second square
sam.penup()
sam.forward(25)
sam.right(90)
sam.forward(25)
sam.pencolor("#2ED14F")
sam.pensize(1)
sam.pendown()
# Draw second square
while count < 4:
    sam.forward(150)
    sam.left(90)
    count += 1

win.mainloop()
