from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("the SnAkE Game")
screen.tracer(0)
snake = Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    if snake.segments[0].distance(food)<15:
        score.increament()
        food.refresh()
        snake.extend()
    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290:
        score.gameover()
        game_is_on=False
    for segment in range(1,len(snake.segments)):
        if snake.segments[0].distance(snake.segments[segment])<8:
            game_is_on=False
            score.gameover()
screen.exitonclick()
