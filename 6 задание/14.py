from turtle import *
screensize(10000, 10000)
tracer(0)
k = 50
left(90)
for i in range(11):
    fd(4 * k)
    rt(60)
pu()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        dot(3)
home()
pd()
goto(20 * k, 0)
goto(-20 * k, 0)
update()
done()