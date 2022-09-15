from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.turn_north, 'Up')
screen.onkey(snake.turn_south, 'Down')
screen.onkey(snake.turn_east, 'Right')
screen.onkey(snake.turn_west, 'Left')

score.appear()


def game_over():
    segment = Turtle(visible=False)
    segment.goto(-60, 0)
    segment.color('red')
    segment.write('Game over', align='left', font=('Arial', 20, 'normal'))


game_is_on = True
while game_is_on and snake.no_intersections():
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    print(snake.get_positions())
    if snake.head.distance(food) < 5:
        food.respawn()
        snake.grow()
        score.change()
        score.clearing()
        score.appear()
    if abs(snake.head.pos()[0]) > 300 or abs(snake.head.pos()[1]) > 300:
        screen.reset()
        game_is_on = False

game_over()


screen.exitonclick()
