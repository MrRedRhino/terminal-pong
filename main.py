import shutil
import keyboard
import curses
import time
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
            if ball.pos[1] - 4 < left_racket.pos[1] or ball.pos[1] + 4 > left_racket.pos[1]:
                score[0] += 1

        # if ball.pos[0] + 6 > screen_size[0]:
        #     score[1] += 1

        left_racket.draw()
        right_racket.draw()
        ball.move()

        # if ball.pos[0] in [screen_size[0] - 3, screen_size[0] - 4, 1, 0]:
        #     if not right_racket.pos[1] - 1 < ball.pos[1] + 1 < right_racket.pos[1] + 5:
        #         score[0] += 1
        #         ball.pos = [int(screen_size[0] / 2), int(screen_size[1] / 2)]
        #     if not left_racket.pos[1] - 1 < ball.pos[1] + 1 < left_racket.pos[1] + 5:
        #         score[1] += 1
        #         ball.pos = [int(screen_size[0] / 2), int(screen_size[1] / 2)]

        handle_points(stdscreen)
        
        stdscreen.refresh()
        stdscreen.clear()
        # time.sleep(0.03)
        time.sleep(0.03)


if shutil.get_terminal_size().columns < 80 or shutil.get_terminal_size().lines < 24:
    print(f'Your terminal-screen has to be at least 80x24 characters big')
    quit()

screen_size = [shutil.get_terminal_size().columns, shutil.get_terminal_size().lines]

curses.wrapper(main)
