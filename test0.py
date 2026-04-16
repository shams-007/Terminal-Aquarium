import time
import os

class Fish:
    def __init__(self, x, y, vx, vy,):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    
    def move(self, width):
        self.x += self.vx
        self.y += self.vy
        self.border(width)

    def border(self, width):
        if self.x >= width or self.x <= 0:
            self.vx *= -1
    
    def show(self):
        print(self.x, self.y)


nemo = Fish(3, 20, 1 , 1)
dory = Fish(10, 17, 1, 1)