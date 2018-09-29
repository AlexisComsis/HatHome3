from gameobject import *
from movemap import *

class Player(Game_object):

    def __init__(self, hp_limit, speed, imageup, bank_image, x, y):
        Game_object.__init__(self, imageup, bank_image, x, y)
        self.speed = speed
        self.hp_limit = hp_limit
        self.hp = hp_limit


    def be(self, window, keys, mouse, click):
        self.control(keys)
        window.blit(self.imageup,(self.x, self.y))



    def control(self, keys):
        #UP
        if keys[pygame.K_w]:
            if keys[pygame.K_a]:
                Movemap.upleft(self.speed)
                self.upleft()
            elif keys[pygame.K_d]:
                Movemap.upright(self.speed)
                self.upright()
            else:
                Movemap.up(self.speed)
                self.up()

        #DOWN
        elif keys[pygame.K_s]:
            if keys[pygame.K_a]:
                Movemap.downleft(self.speed)
                self.downleft()
            elif keys[pygame.K_d]:
                Movemap.downright(self.speed)
                self.downright()
            else:
                Movemap.down(self.speed)
                self.down()

        #LEFT
        elif keys[pygame.K_a]:
            Movemap.left(self.speed)
            self.left()

        #RIGHT
        elif keys[pygame.K_d]:
            Movemap.right(self.speed)
            self.right()


    timer1 = 0
    def animation(self, spr1, spr2):
        Player.timer1 += 1

        if Player.timer1 <= 15:
            self.imageup = self.bank_image[spr1]
        elif Player.timer1 <= 31:
            self.imageup = self.bank_image[spr2]
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
