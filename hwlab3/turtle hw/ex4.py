from turtle import *
from ex3_0 import *



for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()



mainloop()