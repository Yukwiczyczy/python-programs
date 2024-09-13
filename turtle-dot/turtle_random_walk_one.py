from turtle import Turtle, Screen
import random

howard_turtle = Turtle()

# Change a new shape and color
howard_turtle.shape('turtle')
howard_turtle.color('green')

# Turtle movement to draw multiple shapes from triangle to dodecagon
def random_walk():
    howard_turtle.pen(pensize=2)

    def random_color():
        color = tuple(random.random() for _ in range(3))
        return color
    
    def turn_and_move():
        r, g, b = random_color()
        howard_turtle.color(r, g, b)
        
        distances = [30, 60]
        howard_turtle.forward(random.choice(distances))
        
        directions = [-90, 90]
        howard_turtle.right(random.choice(directions))

    while True:
        turn_and_move()
  
random_walk()
            
screen = Screen()
screen.exitonclick()