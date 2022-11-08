from turtle import *
screensize(10000, 10000)
tracer(0)
k = 70
left(90)
for i in range(16):
    lt(36)
    fd(4 * k)
    lt(36)
pu()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(3)
update()
done()