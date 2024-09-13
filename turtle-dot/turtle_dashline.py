from turtle import Turtle, Screen

howard_turtle = Turtle()

# Change a new shape and color
howard_turtle.shape('arrow')
howard_turtle.color('green')

# Turtle movement to draw dashline
def create_dashline():
    howard_turtle.penup()
    howard_turtle.setx(-200)
    
    for i in range(13):
        howard_turtle.pendown()
        howard_turtle.forward(20)
        howard_turtle.penup()
        howard_turtle.forward(20)

create_dashline()
        
screen = Screen()
screen.exitonclick()