import turtle
import random

# Set up the turtle screen
turtle.speed(2)
turtle.bgcolor("white")
turtle.title("Random Turtle Drawing")

# Function to draw a random pattern
def draw_random_pattern():
    for _ in range(50):
        # Set random colors
        turtle.pencolor(random.random(), random.random(), random.random())
        
        # Set random position
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        
        # Draw a random shape (circle or square)
        shape = random.choice(["circle", "square"])
        if shape == "circle":
            radius = random.randint(10, 50)
            turtle.circle(radius)
        elif shape == "square":
            side_length = random.randint(10, 50)
            for _ in range(4):
                turtle.forward(side_length)
                turtle.left(90)

# Draw the random pattern
draw_random_pattern()

# Close the turtle graphics window on click
turtle.exitonclick()
