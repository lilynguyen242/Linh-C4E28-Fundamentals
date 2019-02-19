from turtle import *
# speed(100)
shape('turtle')

for i in range(3):
    for e in range(4):
        forward(100)
        left(90)
    left(60)
color("black", "pink")
begin_fill()
# for i in range(4):
#         forward(50)
#         penup()
#         forward(50)
#         pendown()
#         left(90)

circle(100)

end_fill()
mainloop()