import turtle

turtle.speed(100)
turtle.pensize(5)

turtle.screensize(600, 600)
turtle.pencolor('dark blue')
turtle.forward(50)
turtle.goto(100, -175)
turtle.pu()
turtle.goto(400, -250)
turtle.pd()
turtle.goto(125, -250)
turtle.goto(100, -200)
turtle.goto(400, -200)
turtle.goto(450, -50)
turtle.goto(70, -50)


def circleb(x, y, r, color):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.circle(r)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.end_fill


circleb(200, -325, 25, 'dark blue')
circleb(350, -325, 25, 'dark blue')

turtle.pu()
turtle.goto(120, -50)
turtle.pencolor('light blue')
turtle.pd()
turtle.goto(150, -200)
turtle.pu()
turtle.goto(250, -50)
turtle.pd()
turtle.goto(250, -200)
turtle.pu()
turtle.goto(370, -50)
turtle.pd()
turtle.goto(340, -200)
turtle.pu()
turtle.goto(80, -100)
turtle.pd()
turtle.goto(425, -100)
turtle.pu()
turtle.goto(90, -150)
turtle.pd()
turtle.goto(420, -150)
