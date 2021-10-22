import shutil


class Racket:
    def __init__(self, screen, left, screen_width):
        self.pos = [0, 0]
        if left:
            self.pos[0] = 2
        else:
            self.pos[0] = screen_width - 3
        self.screen = screen
    
    def draw(self):
        for i in range(4):
            self.screen.addstr(self.pos[1] + i, self.pos[0], '|')
    
    def move(self, dir):
        if dir == 'up' and self.pos[1] > 0:
            self.pos[1] -= 1
        elif dir == 'down' and self.pos[1] + 4 < shutil.get_terminal_size().lines:
            self.pos[1] += 1
