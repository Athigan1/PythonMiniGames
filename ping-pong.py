# PING PONG GAME BY ATHIGAN SINNATHURAI
import turtle

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Player 1
player_1 = turtle.Turtle()
player_1.shapesize(stretch_wid=4, stretch_len=1)
player_1.speed(0)
player_1.shape("square")
player_1.color("white")
player_1.penup()
player_1.goto(-350, 0)

# Player 2
player_2 = turtle.Turtle()
player_2.shapesize(stretch_wid=4, stretch_len=1)
player_2.speed(0)
player_2.shape("square")
player_2.color("white")
player_2.penup()
player_2.goto(350, 0)

# ping pong ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# score
score_1 = 0
score_2 = 0

overhead = turtle.Turtle()
overhead.speed(0)
overhead.color("yellow")
overhead.penup()
overhead.hideturtle()
overhead.goto(0, 280)
overhead.write("Player 1: 0  Player 2: 0", align="center", font=("Comic Sans MS", 12, "normal"))


# Player 1 movements
def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)


def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)


# Player 2 movements
def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)


def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)


# Movement controls
wn.listen()
wn.onkeypress(player_1_up, "q")
wn.onkeypress(player_1_down, "z")
wn.onkeypress(player_2_up, "Up")
wn.onkeypress(player_2_down, "Down")

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Define BorderS
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_1 += 1
        overhead.clear()
        overhead.write(f"Player 1: {score_1}  Player 2: {score_2}", align="center",
                       font=("Comic Sans MS", 12, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_2 += 1
        overhead.clear()
        overhead.write(f"Player 1: {score_1}  Player 2: {score_2}", align="center",
                       font=("Comic Sans MS", 12, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() == 350 and player_2.ycor() - 40 < ball.ycor() < player_2.ycor() + 40:
        ball.dx *= -1

    if ball.xcor() == -350 and player_1.ycor() - 40 < ball.ycor() < player_1.ycor() + 40:
        ball.dx *= -1
