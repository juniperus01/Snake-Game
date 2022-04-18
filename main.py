from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# setting up our screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# create snake body

#chindi code below
# segment_1 = Turtle(shape="square")
# segment_1.color("white")
#
# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(x=-20, y=0)
#
# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(x=-40, y=0)

screen.tracer(0) # no updates would be visible on the screen even though our code is working
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# control the Snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# move the snake
game_is_on = True
while game_is_on:
    screen.update()  # tracer is off. Therefore we need to manually update the screen for changes to be shown
    time.sleep(0.1)  # to delay every update by one sec
    snake.move()

    # Detect the collision of snake with food
    if snake.snake_head.distance(food) < 15: # food is 10 by 10. So we add a little buffer of 5
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail

    #if-elif wala chindi code

    # for segment in snake.segments:
    #     if segment == snake.snake_head:
    #         pass
    #     elif snake.snake_head.distance(segment) < 10:
    #         game_is_on = False

    # better code
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # if head collides with any segment in the tail: trigger game_over
screen.exitonclick()

