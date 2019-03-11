from turtle import *
def draw_square(length, colour):
    color(colour)
    for i in range(4):
        left(90)
        forward(length)
draw_square(100, "pink")


for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()