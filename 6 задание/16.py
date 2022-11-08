from turtle import *
screensize(10000, 10000)
tracer(0)
k = 50
left(90)
rt(45)

for i in range(9):
    fd(9 * k)
    rt(90)
pu()
for x in range(-10, 20):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(3)
update()
done()