import turtle
win = turtle.Screen()
samJr = turtle.Turtle()

# Initial display options
win.bgcolor("#F6D0E2")
samJr.pensize(3)
samJr.pencolor("#953A55")
samJr.shape("turtle")

# Position for letter K
samJr.penup()
samJr.setpos(-250.00,0.00)
samJr.pendown()
samJr.left(90)
# Draw K
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

# Position for letter J

win.mainloop()
