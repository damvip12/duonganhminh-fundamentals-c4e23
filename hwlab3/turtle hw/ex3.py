from turtle import *
shape("turtle")


def draw_square(length,given_color):
    
    for i in range(4):
        color(given_color)
        forward(length)
        left(90)
    return length, given_color

    

draw_square(100,'red')




mainloop()