import pygame

class Background:

    def __init__(self, image, x, y):
        self.image = image
        self.speed = speed
        self.x = x
        self.y = y

    def be(self, window,  keys):
        window.blit(self.image,(self.x, self.y))
