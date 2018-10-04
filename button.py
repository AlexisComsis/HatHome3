import pygame
from tools import *

class Button:

    def __init__(self, x, y, img_false, img_true):

        self.coord = tools.convert_coord(x, y)
        self.img = [img_false, img_true]
        self.size = [self.img[0].get_width(), self.img[0].get_height()]
        self.run_variable = True

    def activate(self, window, mouse, click):

        if self.run_variable:
            if self.coord[0] + self.size[0] > mouse[0] > self.coord[0] and self.coord[1] + self.size[1] > mouse[1] > self.coord[1]:
                window.blit(self.img[0], (self.coord[0], self.coord[1]))
                if click[0] == 1:
                    self.run_variable = False
            else:
                window.blit(self.img[1], (self.coord[0], self.coord[1]))
        else:
            window.blit(self.img[0], (self.coord[0], self.coord[1]))
