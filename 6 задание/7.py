from turtle import *
screensize(10000, 10000)
tracer(0)
k = 50
for i in range(15):
    goto(xcor() + 10 * k, ycor() + 10 * k)
    goto(xcor() + 3 * k, ycor() - 6 * k)
    goto(xcor() - 9 * k, ycor() + 3 * k)
pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)
update()
done()
print(16 * 15 + 1)