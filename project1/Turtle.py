import turtle

t = turtle.Turtle()
ts = t.getscreen()
t.shape("turtle")
t.color("yellow")
ts.bgcolor("black")

def move():
    t.forward(20)

def turn_left():
    t.left(90)

def turn_right():
    t.right(90)

ts.onkey(move, "space")
ts.onkey(turn_left, "a")
ts.onkey(turn_right, "s")

ts.listen()

turtle.done()