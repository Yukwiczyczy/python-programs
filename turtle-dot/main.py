import dis
from turtle import Turtle, Screen
import random

howard_turtle = Turtle()

# Change a new shape and color
howard_turtle.shape('turtle')
howard_turtle.color('green')

# Turtle movement to draw square
def create_square():
    
    for i in range(4):
        howard_turtle.forward(100)
        howard_turtle.right(90)


def create_dashline():
    howard_turtle.penup()
    howard_turtle.setx(-500)
    
    for i in range(13):
        howard_turtle.pendown()
        howard_turtle.forward(20)
        howard_turtle.penup()
        howard_turtle.forward(20)


def create_complex_shapes():
    max_sides = 8
    
    starting_count = 3
    for draw in range(max_sides):
        angle_turn = int(360/starting_count)
        
        # random_number = random.randint(0, 256)
        random_color = tuple (random.random() for _ in range(3))
        print(random_color)
        x,y,z = random_color
        howard_turtle.color(z,y,z)
        
        for _ in range(starting_count):
            howard_turtle.forward(100)
            howard_turtle.right(angle_turn)
            
        starting_count += 1
 
    
def turn_left(trigger):
    if trigger == 1:
        howard_turtle.left(90)
        howard_turtle.forward(20)
    
    
def turn_right(trigger):
    if trigger == 1:
        howard_turtle.right(90)
        howard_turtle.forward(20)

    
def random_walk():
    while True:
        turns = [turn_left, turn_right]
        random_color = tuple (random.random() for _ in range(3))

        # Change color
        x,y,z = random_color
        howard_turtle.color(z,y,z)
        selected_method = random.choice(turns)
        howard_turtle.color()
        
        # Change line size
        howard_turtle.pen(pensize=10)
        
        selected_method(1)
        
        
def another_random_walk():
    directions = [0, 90, 180, 360]
    distance = [10, 20, 30, 40]
    
    howard_turtle.pen(pensize=8)
    
    def random_color():
        colors = ['red', 'yellow', 'blue', 'green', 'violet', 'orange', 'indigo']
        howard_turtle.color(random.choice(colors))
    
    def move():
        random_color()
        howard_turtle.forward(random.choice(distance))
        howard_turtle.setheading(random.choice(directions))
        
    while True:
        move()
        
    
# show screen
screen = Screen()
screen.exitonclick()