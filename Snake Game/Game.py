from turtle import Screen
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

scoreboard = Scoreboard()
playing = True

while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting collision with food. using the distance attribute
    if snake.head.distance(food) < 15:
        food.food_refresh()
        scoreboard.increase_score()
        snake.extend_body()

    #Detecting collision with walls of the game
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295 :
        playing = False
        scoreboard.game_over()

    #Detecting collision with self i.e tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            playing = False
            scoreboard.game_over()
            

