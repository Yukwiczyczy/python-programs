from turtle import Turtle, Screen

howard_turtle = Turtle()

# Change a new shape and color
howard_turtle.shape('arrow')
howard_turtle.color('green')

# Turtle movement to draw square
def create_square():
    
    for i in range(4):
        howard_turtle.forward(100)
        howard_turtle.right(90)
        
create_square()
        
screen = Screen()
screen.exitonclick()