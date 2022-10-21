from turtle import *
screensize(10000, 10000)
tracer(0)
k = 50
for i in range(10):
    goto(xcor() - 6 * k, ycor() + 9 * k)
    goto(xcor() + 6 * k, ycor() - 2 * k)
    goto(xcor() - 3 * k, ycor() - 6 * k)
pu()
for x in range(-40, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)
update()
done()