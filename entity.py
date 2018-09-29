from gameobject import *

class Entity(Game_object):

    list_object_inrun = []
    list_object_phys = []
    def __init__(self, imageup, bank_image, x, y, phys):
        Game_object.__init__(self, imageup, bank_image, x, y)
        Entity.list_object_inrun.append(self)
        if phys:
            Entity.list_object_phys.append(self)
