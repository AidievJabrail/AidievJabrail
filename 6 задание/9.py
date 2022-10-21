from turtle import *
screensize(10000, 10000)
tracer(0)
k = 50
for i in range(7):
    goto(xcor() + 6 * k, ycor() - 9 * k)
    goto(xcor() - 6 * k, ycor() + 2 * k)
    goto(xcor() + 12 * k, ycor() + 3 * k)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)
update()
done()
print(7 * 7 + 1)