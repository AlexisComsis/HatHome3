

    def updater(self):
        Entity.timer1 += 1
        if Entity.timer1 < 65:
            self.state = 0
        elif Entity.timer1 < 90:
            self.state = 1
        else:
            Entity.timer1 = 0

--------------------------------------------

from tools import *
class Game_object:
    """
    All entity who get an x and y and can be
    """
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def be(self, window):
        window.blit(self.image,(self.x, self.y))
-----------------------------------------------
from living import *

class Player(Living):

    def __init__(self, x, y, image, hp_limit, speed, sprite):
        Living.__init__(self, x, y, image, hp_limit, speed)
        self.sprite = sprite
        self.speed = speed

    def be(self, window, keys, mouse, click):
        self.control(keys)
        window.blit(self.image,(self.x, self.y))

    #0 = front
    #1 = right1
    #2 = right2
    #3 = left1
    #4 = left2
    #5 = down1
    #6 = down2
    #7 = up1
    #8 = up2
    #9 = upright1
    #10 = upright2
    #11 = upleft1
    #12 = upleft2
    #13 = downright1
    #14 = downright2
    #15 = downleft1
    #16 = downleft2

    def control(self, keys):
        #UP
        if keys[pygame.K_w]:
            if keys[pygame.K_a]:
                self.upleft()
            elif keys[pygame.K_d]:
                self.upright()
            else:
                self.up()

        #DOWN
        elif keys[pygame.K_s]:
            if keys[pygame.K_a]:
                self.downleft()
            elif keys[pygame.K_d]:
                self.downright()
            else:
                self.down()

        #LEFT
        elif keys[pygame.K_a]:
            self.left()

        #RIGHT
        elif keys[pygame.K_d]:
            self.right()

    timer1 = 0
    def animation(self, spr1, spr2):
        Player.timer1 += 1

        if Player.timer1 <= 5:
            self.image = self.sprite[spr1]
        elif Player.timer1 <= 11:
            self.image = self.sprite[spr2]
        else:
            Player.timer1 = 0

    def up(self):
        self.animation(7,8)

    def upleft(self):
        self.animation(11,12)

    def upright(self):
        self.animation(9,10)

    def down(self):
        self.animation(5,6)

    def downleft(self):
        self.animation(15,16)

    def downright(self):
        self.animation(13,14)

    def left(self):
        self.animation(3,4)

    def right(self):
        self.animation(1,2)
------------------------------------------
from entity import *

class Living(Entity):

    def __init__(self, x, y, image, hp_limit, speed):
        Entity.__init__(self, x, y, image)
        self.hp_limit = hp_limit   # Max health points
        self.hp = hp_limit # Health points
        self.speed = speed

    def updater(self):
        pass
------------------------------------------
