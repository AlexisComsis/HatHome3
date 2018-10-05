from gameobject import *
from movemap import *

class Player(Game_object):

    def __init__(self, hp_limit, speed, imageup, bank_image, x, y):
        Game_object.__init__(self, imageup, bank_image, x, y)
        self.speed = speed
        self.hp_limit = hp_limit
        self.hp = hp_limit
        self.colisionside = None
        self.centerp = None


    def be(self, window, keys, mouse, click):
        self.control(keys)
        window.blit(self.imageup,(self.x, self.y))
        self.colisionside = None

    def collision(self):
        self.centerp = (self.center[0] + self.x, self.center[1] + self.y)
        for object in Entity.list_object_phys:
            object.centerp = (object.center[0] + int(object.x), object.center[1] + int(object.y))

            if (self.centerp[0] + self.center[0]  >= object.centerp[0] - object.center[0] and self.centerp[0] - self.center[0] <= object.centerp[0] + object.center[0]) and\
                (self.centerp[1]  >= object.centerp[1] - object.center[1] and  self.centerp[1]  <= object.centerp[1] + object.center[1]):
        #[0] = x  ;  [1] = y
                self.objectconflict = object
                return(True)

        return(False)

    def strongest(self, flag1, flag2):


        x = self.centerp[0] - self.objectconflict.centerp[0]
        x = abs(x)
        y = self.centerp[1] - self.objectconflict.centerp[1]
        y = abs(y)

        if y > x:
            if flag1 == "down":
                Movemap.down(self.speed//3)
            else:
                Movemap.up(self.speed//3)
        else:
            if flag2 == "left":
                Movemap.left(self.speed//3)
            else:
                Movemap.right(self.speed//3)

    def control(self, keys):

        #UP
        if keys[pygame.K_w]:
            if keys[pygame.K_a]:
                Movemap.upleft(self.speed)
                self.upleft()
                if self.collision():
                    Movemap.downright(self.speed)
                    ctest = self.strongest("down", "right")

            elif keys[pygame.K_d]:
                Movemap.upright(self.speed)
                self.upright()
                if self.collision():
                    Movemap.downleft(self.speed)
                    ctest = self.strongest("down", "left")

            else:
                Movemap.up(self.speed)
                self.up()
                if self.collision():
                    Movemap.down(self.speed)

        #DOWN
        elif keys[pygame.K_s]:
            if keys[pygame.K_a]:
                Movemap.downleft(self.speed)
                self.downleft()
                if self.collision():
                    Movemap.upright(self.speed)
                    ctest = self.strongest("up", "right")

            elif keys[pygame.K_d]:
                Movemap.downright(self.speed)
                self.downright()
                if self.collision():
                    Movemap.upleft(self.speed)
                    ctest = self.strongest("up", "left")
            else:
                Movemap.down(self.speed)
                self.down()
                if self.collision():
                    Movemap.up(self.speed)

        #LEFT
        elif keys[pygame.K_a]:
            Movemap.left(self.speed)
            self.left()
            if self.collision():
                Movemap.right(self.speed)

        #RIGHT
        elif keys[pygame.K_d]:
            Movemap.right(self.speed)
            self.right()
            if self.collision():
                Movemap.left(self.speed)



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
