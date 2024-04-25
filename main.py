from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring='snake game')
screen.tracer(0)

snake = Snake()
food_obj = Food()
score_obj = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    # Detect collisions with food
    if snake.head.distance(food_obj) < 15:
        food_obj.refresh()
        snake.extend()
        score_obj.increase_score()

    # Detect collisions with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score_obj.game_over()

    # Detect collisions with body
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            score_obj.game_over()
screen.exitonclick()
