import turtle

def drawSquare(t, sz):
    """Get turtle t to draw of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

wn.exitonclick()