import turtle
import datetime

def main():
    turtle.tracer(False)
    turtle.mode('logo') # resets turtle heading to north
    tickHand('second', 150)
    tickHand('minute', 120)
    tickHand('hour', 88)
    #shape of hands
    second = turtle.Turtle()
    second.shape('second')
    second.shapesize(1, 1, 3)
    second.speed(0)
    minute = turtle.Turtle()
    minute.shape('minute')
    minute.shapesize(3, 3, 3)
    minute.speed(0)
    hour = turtle.Turtle()
    hour.shape('hour')
    hour.shapesize(6, 6, 3)
    hour.speed(0)


if __name__ == '__main__':
    main()