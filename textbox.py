from entity import *
from load import *


class Box:
    def display(self,window): #text is string
        '''
        show the box above a entity
        '''
        window.blit(textbox, (200,750))
