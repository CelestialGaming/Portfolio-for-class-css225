import turtle
Tom = turtle.Turtle ()#or t.Turtle

potato = input("do you want to do a triangle or square")

if potato == ("triangle"):

    triangle_side = int(input("Please insert number for triangle", ))

    #for number
    Tom.pencolor("red")
    Tom.fillcolor("purple")
    Tom.begin_fill()
    for number in range(1,4):
        Tom.forward(triangle_side)
        Tom.right(120)
    Tom.end_fill()

elif potato == ("square"):

    square_side = int(input("please insert number for square", ))

    Tom.pencolor("blue")
    Tom.fillcolor("gray")
    Tom.begin_fill()
    for number in range(1,5):
        Tom.forward(square_side)
        Tom.right(90)
    Tom.end_fill()

input()