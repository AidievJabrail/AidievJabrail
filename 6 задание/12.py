from turtle import *
screensize(10000, 10000)
tracer(0)
k = 10
left(90)
fd (200 * k)
for i in range(4 ):
    rt(90)
    fd(50 * k)
pu()
for x in range(60):
    for y in range(201):
        goto(x * k, y * k)
        dot(3)
update()
done()
print(49 * 49)