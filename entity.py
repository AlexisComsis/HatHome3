from gameobject import *

class Entity(Game_object):

    list_object_inrun = []
    def __init__(self, imageup, bank_image, x, y):
        Game_object.__init__(self, imageup, bank_image, x, y)
        Entity.list_object_inrun.append(self)
