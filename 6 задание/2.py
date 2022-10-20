from turtle import *
screensize(10000, 10000)
tracer(0)
k = 50
left(90)
for i in range(15):
    forward(15 * k)
    right(120)
pu()
for x in range(30):
    for y in range(30):
        goto(x * k, y * k)
        dot(3)
done()


