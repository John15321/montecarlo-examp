from random import uniform
from math import sqrt
from turtle import *
from time import time

title('Monte Carlo Pi')
setup(width = 640, height = 480)
bgcolor('black')
penup()
hideturtle()
speed(0)

def make_dot(dot_color):
    goto(round(x * 100 - 100), round(y * 100 - 100))
    dot(3, dot_color)

a = b = 1 #circle centre
circ = square = 0

start = time()
for i in range(1, 10001):
    x = uniform(0, 2)
    y = uniform(0, 2)
    r = sqrt((x - a)**2 + (y - b)**2)
    if r <= 1:
        circ += 1
        make_dot('red')
    else:
        square += 1
        make_dot('yellow')
    print('[{}] {}'. format(i, 4*circ/(circ+square)))
end = time()
timer = end - start
print('czas:', timer, 'sekund')
done()
