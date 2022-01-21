from turtle import Screen, Turtle
import time
from Snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

eat = Food()
score_no = Score()

game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move_snake()

	#Food Collision
	if snake.head.distance(eat) < 15:
		eat.refresh()
		score_no.inc_score()
		score_no.display()
		snake.extend()

	#Wall Collision
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		score_no.reset()
		snake.reset()

	#Tail Collision
	for segment in snake.segments:
		if segment == snake.head:
			pass
		elif snake.head.distance(segment) < 10:
			score_no.reset()
			snake.reset()

screen.exitonclick()