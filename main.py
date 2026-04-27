import turtle
import time
import random

# Game Setup
win = turtle.Screen()
win.title("Simple Snake")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Snake Head
head = turtle.Turtle("square")
head.color("green")
head.penup()
head.direction = "stop"

# Food
food = turtle.Turtle("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Movement Logic
def move():
    if head.direction == "up": head.sety(head.ycor() + 20)
    if head.direction == "down": head.sety(head.ycor() - 20)
    if head.direction == "left": head.setx(head.xcor() - 20)
    if head.direction == "right": head.setx(head.xcor() + 20)

def go_up(): head.direction = "up"
def go_down(): head.direction = "down"
def go_left(): head.direction = "left"
def go_right(): head.direction = "right"

win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

# Main Loop
while True:
    win.update()

    # Check for wall collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        head.goto(0, 0)
        head.direction = "stop"

    # Check for food collision
    if head.distance(food) < 20:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

    move()
    time.sleep(0.1)