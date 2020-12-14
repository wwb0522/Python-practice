import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import easygui

def timerHandler():
    global time
    time = time + 1

def draw(canvas):
    global time, color
    D = time % 10
    B = (time // 100) % 6
    C = (time // 10) % 10
    A = time // 600
    timing =  str(A) + ':' + str(B) + str(C) + '.' + str(D)
    canvas.draw_text(timing, (25, 100), 50, color)

def Start():
    global timer, color
    if not timer.is_running():
        timer.start()

def Stop():
    global timer, color
    timer.stop()
    color = 'red'

def Clear():
    global time, color
    if not timer.is_running():
        time = 0
        color = 'white'
    else:
        easygui.msgbox("Timer still running! Please stop it first", title="Warning!!")

def Alarm():
    pass
        

def main():
    global time, color
    time = 0
    color = 'white'
    frame = simplegui.create_frame('My Timer', 200, 200, 100)
    global timer
    timer = simplegui.create_timer(1, timerHandler)
    frame.set_draw_handler(draw)
    frame.add_button('Start', Start, 100)
    frame.add_button('Stop', Stop, 100)
    frame.add_button('Clear', Clear, 100)
    frame.add_button('Set Alarm', Alarm, 100)

    frame.start()

if __name__ == '__main__':
    main()