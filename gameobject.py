from tools import *
import pygame

class Game_object:

    """
    All object in the game
    """

    def __init__(self, imageup, bank_image, x, y):
        self.x = x
        self.y = y
        self.imageup = imageup
        self.bank_image = bank_image

    def be(self, window):
        window.blit(self.imageup,(self.x, self.y))
