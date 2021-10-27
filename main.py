import shutil
import keyboard
import curses
from time import sleep
from ball import Ball
from racket import Racket
from font_handler import get_char


score = [0, 0]
screen_size = [0, 0]


def handle_points(stdscreen):
    global score
    point_str = get_char([str(score[0]), ':', str(score[1])])
    position = int(screen_size[0] / 2) - 10
    stdscreen.addstr(2, position, point_str[0])
    stdscreen.addstr(3, position, point_str[1])
    stdscreen.addstr(4, position, point_str[2])
    stdscreen.addstr(5, position, point_str[3])
    stdscreen.addstr(6, position, point_str[4])


def main(stdscreen):
    global score
    has_scored = False
    ball = Ball(stdscreen, screen_size)
    left_racket = Racket(stdscreen, True, screen_size[0])
    right_racket = Racket(stdscreen, False, screen_size[0])

    while True:
        if keyboard.is_pressed('w'):
            left_racket.move('up')
        if keyboard.is_pressed('s'):
            left_racket.move('down')
        if keyboard.is_pressed('o'):
            right_racket.move('up')
        if keyboard.is_pressed('l'):
            right_racket.move('down')
        
        for i in range(screen_size[1]):
            stdscreen.addstr(i, int(screen_size[0] / 2), '|')
        if ball.pos[0] < 3:
            if not ball.pos[1] - 2 < left_racket.pos[1] or not ball.pos[1] + 6 > left_racket.pos[1]:
                score[0] += 1
                ball.pos = [int(screen_size[0] / 2), int(screen_size[1] / 2)]
                has_scored = True

        if ball.pos[0] + 6 > ball.screen_size[0]:
            if not ball.pos[1] - 2 < right_racket.pos[1] or not ball.pos[1] + 6 > right_racket.pos[1]:
                score[0] += 1
                ball.pos = [int(screen_size[0] / 2), int(screen_size[1] / 2)]
                has_scored = True

        left_racket.draw()
        right_racket.draw()
        ball.move()

        handle_points(stdscreen)
        
        stdscreen.refresh()
        stdscreen.clear()
        if has_scored:
            sleep(1)
            has_scored = False
        else:
            sleep(0.035)

screen_size = [shutil.get_terminal_size().columns, shutil.get_terminal_size().lines]

curses.wrapper(main)
