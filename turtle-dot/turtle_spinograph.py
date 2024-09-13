from turtle import Turtle, Screen
import random

howard_turtle = Turtle()

# Change a new shape and color
howard_turtle.shape('arrow')
howard_turtle.color('green')

# Turtle movement to draw multiple shapes from triangle to dodecagon
def draw_spinograph():
    howard_turtle.pen(pensize=2)

    def random_color():
        color = tuple(random.random() for _ in range(3))
        return color
    
    def draw_circle():
        r, g, b = random_color()
        howard_turtle.color(r, g, b)
        
        howard_turtle.speed(0)
        howard_turtle.circle(100)

    for _ in range(int(360/10)):
        draw_circle()
        howard_turtle.right(10)

draw_spinograph()
            
screen = Screen()
screen.exitonclick()