import turtle

# ===================== Window Design ========================= #
window = turtle.Screen()
window.setup(width = 800, height = 600)
window.bgcolor(0.2,0.2,0.2)
window.title("Ping Pong Game By Hana Elfar")
window.tracer(0)  # Stop the window from updating automatically

# ===================== Objects Design ======================== #
ball = turtle.Turtle()
ball.shape("circle")  
ball.color("white")
ball.speed(0)
ball.goto(x = 0, y = 0)
ball.penup()
ball.dx, ball.dy = 0.2, 0.2

center_line = turtle.Turtle()
center_line.shape("square")
center_line.color("white")
center_line.speed(0)
center_line.shapesize(stretch_len = 0.1, stretch_wid = 26)
center_line.goto(x = 0, y = 0)
center_line.penup()

player1 = turtle.Turtle()
player1.shape("square")
player1.color("blue")
player1.speed(0)
player1.shapesize(stretch_len = 0.7, stretch_wid = 5)
player1.penup()
player1.goto(x = -350, y = 0)

player2 = turtle.Turtle()
player2.shape("square")
player2.color("red")
player2.speed(0)
player2.shapesize(stretch_len = 0.7, stretch_wid = 5)
player2.penup()
player2.goto(x = 350, y = 0)

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.goto(x = 0, y = 260)
score.write("Player 1 : 0 Player 2 : 0 ", align = "center", font = ("courier", 14, "normal"))
score.hideturtle()
score.penup()
p1_score, p2_score = 0, 0 

# ==================== Players Movement ====================== #
players_speed = 20

def p1_move_up():
  player1.sety(player1.ycor() + players_speed)

def p1_move_down():
  player1.sety(player1.ycor() - players_speed)

def p2_move_up():
  player2.sety(player2.ycor() + players_speed)

def p2_move_down():
  player2.sety(player2.ycor() - players_speed)


# def p1_move_up():
#   if player1.ycor() + players_speed > 300:
#     player1.sety(300)
#   else:
#     player1.sety(player1.ycor() + players_speed)

# def p1_move_down():
#   if player1.ycor() - players_speed < -300:
#     player1.sety(-300)
#   else:
#     player1.sety(player1.ycor() - players_speed)

# def p2_move_up():
#   if player2.ycor() + players_speed > 300:
#     player2.sety(300)
#   else:
#     player2.sety(player2.ycor() + players_speed)

# def p2_move_down():
#   if player2.ycor() - players_speed < -300:
#     player2.sety(-300)
#   else:
#     player2.sety(player2.ycor() - players_speed)

# ==================== Get Users Inout ======================= #
window.listen()
window.onkeypress(p1_move_up, 'w')
window.onkeypress(p1_move_down, 's')
window.onkeypress(p2_move_up, 'Up')
window.onkeypress(p2_move_down, 'Down')

# ======================= Game Loop ========================== #
while True:
  window.update()

  # Move the Ball
  ball.setx(ball.xcor() + ball.dx )
  ball.sety(ball.ycor() + ball.dy )

  if ball.ycor() > 290:   
    ball.sety(290)
    ball.dy *= -1  

  if ball.ycor() < -290 :   
    ball.sety(-290)
    ball.dy *= -1  

  if(ball.xcor() > 390):
    ball.goto(0, 0)
    ball.dx *= -1  
    score.clear()
    p1_score += 1
    score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center", font=("Courier", 14, "normal"))

  if(ball.xcor() < -390):
    ball.goto(0, 0)
    ball.dx *= -1 
    score.clear()
    p2_score += 1
    score.write(f"Player1: {p1_score} Player2: {p2_score}", align="center", font=("Courier", 14, "normal"))

  # tasadam player and ball
  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > player1.ycor() - 60  and ball.ycor() <  player1.ycor() + 60) :
    ball.setx(-340)
    ball.dx *= -1

  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() > player2.ycor() - 60 and ball.ycor() < player2.ycor() + 60) :
    ball.setx(340)
    ball.dx *= -1
