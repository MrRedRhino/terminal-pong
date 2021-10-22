from pygame import mixer
mixer.init()
mixer.music.load('beep.wav')
mixer.music.play()
mixer.music.set_volume(100)


class Ball:
    def __init__(self, screen, screen_size):
        self.screen_size = screen_size
        self.pos = [10, 10]
        self.screen = screen
        self.direction = 'SO'  # SO, NO, NW, SW

    def draw(self):
        self.screen.addstr(self.pos[1], self.pos[0], '◢ ◣')
        self.screen.addstr(self.pos[1] + 1, self.pos[0], '◥ ◤')

    def move(self):
        if self.direction == 'SO':
            self.pos[0] += 2
            self.pos[1] += 1
        if self.direction == 'NO':
            self.pos[0] += 2
            self.pos[1] -= 1
        if self.direction == 'NW':
            self.pos[0] -= 2
            self.pos[1] -= 1
        if self.direction == 'SW':
            self.pos[0] -= 2
            self.pos[1] += 1
        self.draw()
        self.check_collision()

    def check_collision(self):
        if self.pos[1] + 3 > self.screen_size[1] or self.pos[1] < 1:
            if self.direction == 'SO':
                self.direction = 'NO'
            elif self.direction == 'NO':
                self.direction = 'SO'
            elif self.direction == 'NW':
                self.direction = 'SW'
            else:
                self.direction = 'NW'
            mixer.music.play()

        elif self.pos[0] + 6 > self.screen_size[0] or self.pos[0] < 3:
            if self.direction == 'SO':
                self.direction = 'SW'
            elif self.direction == 'NO':
                self.direction = 'NW'
            elif self.direction == 'NW':
                self.direction = 'NO'
            elif self.direction == 'SW':
                self.direction = 'SO'
            mixer.music.play()
