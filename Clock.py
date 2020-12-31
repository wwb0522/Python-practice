import turtle
import datetime

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def shapeHand(name, length):
    turtle.reset()
    #turtle.penup()
    #turtle.forward(-length * 0.01)
    #turtle.pendown()
    turtle.begin_poly()
    turtle.forward(length)
    turtle.end_poly()
    hand = turtle.get_poly()
    turtle.register_shape(name, hand)

def createClock(radius):
    turtle.reset()
    turtle.pensize(10)
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()
    #adding number
    printer.forward(130)
    printer.write('12', align='center', font=("Courier", 14, "bold"))
    printer.back(285)
    printer.write('6', align='center', font=("Courier", 14, "bold"))
    printer.home()
    printer.right(95)
    printer.forward(150)
    printer.write('3', align='center', font=("Courier", 14, "bold"))
    printer.left(5)
    printer.back(295)
    printer.write('9', align='center', font=("Courier", 14, "bold"))
    #adding date 
    printer.home()
    printer.forward(70)
    printer.write(weekday[datetime.datetime.today().weekday()] , align='center', font=("Courier", 18, "bold"))
    printer.forward(20)
    printer.write(datetime.datetime.today().date() , align='center', font=("Courier", 18, "bold"))
    for i in range(60):
        turtle.penup()
        turtle.forward(radius)
        turtle.pendown()
        if i % 5 == 0:
            turtle.forward(10)
            turtle.penup()
            turtle.forward(-radius-10)
            turtle.pendown()
        else:
            turtle.dot(5)
            turtle.penup()
            turtle.forward(-radius)
            turtle.pendown()
        turtle.right(6)

def startTick(secondHand, minuteHand, hourHand):
    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()
    today = datetime.datetime.today()
    second = today.second 
    minute = today.minute + second / 60
    hour = (today.hour + minute / 60) % 12
    secondHand.setheading(6 * second)
    minuteHand.setheading(6 * minute)
    hourHand.setheading(30 * hour)
    turtle.ontimer(startTick(secondHand, minuteHand, hourHand), 100)


def main():
    turtle.tracer(False)
    turtle.mode('logo') # resets turtle heading to north
    shapeHand('second', 150)
    shapeHand('minute', 125)
    shapeHand('hour', 80)
    #shape of hands
    second = turtle.Turtle()
    second.shape('second')
    second.shapesize(1, 1, 3)
    second.speed(0)
    minute = turtle.Turtle()
    minute.shape('minute')
    minute.shapesize(1, 1, 6)
    minute.speed(0)
    hour = turtle.Turtle()
    hour.shape('hour')
    hour.shapesize(1, 1, 9)
    hour.speed(0)
    createClock(160)
    turtle.tracer(True)
    startTick(second, minute, hour)
    turtle.mainloop()


if __name__ == '__main__':
    main()