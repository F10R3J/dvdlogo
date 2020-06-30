import turtle
screen = turtle.Screen()
screen.bgcolor("blue")
screen.screensize()
screen.setup(width = 1.0, height = 1.0)
# dvd logo
screen.register_shape('dvdlogo.gif')
dvd = turtle.Turtle()
dvd.speed(0)
dvd.shape("dvdlogo.gif")
dvd.color("black")
dvd.penup()
dvd.goto(0,0)
speed = 5
dvd.dx = speed
dvd.dy = speed
cornerhits = 0

# main loop
loop = True
while (loop == True):
    screen.update()

    dvd.setx(dvd.xcor() + dvd.dx)
    dvd.sety(dvd.ycor() + dvd.dy)

    if (dvd.xcor() >= 950):
        dvd.dx = dvd.dx * -1

    if (dvd.xcor() <= -950):
        dvd.dx = dvd.dx * -1

    if (dvd.ycor() >= 590):
        dvd.dy = dvd.dy * -1

    if (dvd.ycor() <= -590):
        dvd.dy = dvd.dy * -1


    if (dvd.xcor() >= 950) and (dvd.ycor() >= 590):
        cornerhits = cornerhits + 1

    if (dvd.xcor() >= 950) and (dvd.ycor() <= -590):
        cornerhits = cornerhits + 1

    if (dvd.xcor() <= -950) and (dvd.ycor() >= 590):
        cornerhits = cornerhits + 1

    if (dvd.xcor() <= -950) and (dvd.ycor() <= -590):
        cornerhits = cornerhits + 1
