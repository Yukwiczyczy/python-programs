from turtle import Turtle, Screen
import random

howard_turtle = Turtle()

# Change a new shape and color
howard_turtle.shape('arrow')
howard_turtle.color('green')

# Turtle movement to draw multiple shapes from triangle to dodecagon
def create_complex_shapes():

    def random_color():
        color = tuple(random.random() for _ in range(3))
        return color
    
    
    def draw_shape(sides):
        for _ in range(sides):
            howard_turtle.forward(50)
            howard_turtle.right(int(360/sides))
            
            
    def draw_shapes():
        howard_turtle.pen(pensize=2)        
        
        starting_side = 3
        for _ in range(10):
            r, g, b = random_color()
            howard_turtle.color(r, g, b)
            
            draw_shape(starting_side)
            starting_side += 1
        
    draw_shapes()
  
create_complex_shapes()
            
screen = Screen()
screen.exitonclick()