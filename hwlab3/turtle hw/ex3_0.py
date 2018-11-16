#Being used in ex4.py . U can check my answer of exercise 3 at ex3.py

from turtle import *
shape("turtle")


def draw_square(length,given_color):
    
    for i in range(4):
        color(given_color)
        forward(length)
        left(90)


    
# draw_square(length,given_color)




