import pygame, time
import AllLevels
wgroup = pygame.sprite.Group()



class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite, mana=0):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((x, y), (64, 64))
        if mana == 0:
            self.image = pygame.image.load(sprite)
        else:
            self.image = pygame.image.load(sprite + "1.png")
            self.baseimage = sprite
            self.num = 1

    def animate(self, tv, sprite):
        if tv % 15 == 0:
            self.baseimage = ""
            self.baseimage = sprite
            self.num += 1
            if self.num > 3:
                self.num = 1
        self.image = pygame.image.load(str(self.baseimage) + str(self.num) + ".png")

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite, a=64, b=64):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, a, b)
        self.image = pygame.image.load(sprite + "D2.png")
        self.list = []
        self.num = 1
        self.baseimage = sprite
        self.kcharge = 0
        self.mcharge = 0
        self.dir = "D"
        for i in range(120):
            self.list.append((x, y))
    def animate(self, tv , sprite="Imigaes/Static/static"):
        if tv % 15 == 0:
            self.baseimage = sprite
            self.num += 1
            if self.num > 4:
                self.num = 1
        self.image = pygame.image.load(str(self.baseimage) + str(self.dir) + str(self.num) + ".png")


    def move(self, xspd, yspd):
        if xspd != 0:
            self.move_a(xspd, 0)
            if xspd > 0:
                self.dir = "R"
            if xspd < 0:
                self.dir = "L"
        if yspd != 0:
            self.move_a(0, yspd)
            if yspd > 0:
                self.dir = "D"
            if yspd < 0:
                self.dir = "U"

    def move_a(self, xspd, yspd):
        self.rect.x += xspd
        self.rect.y += yspd
        for wall in wgroup:
            if self.rect.colliderect(wall.rect):
                if xspd > 0:
                    self.rect.right = wall.rect.left
                if xspd < 0:
                    self.rect.left = wall.rect.right
                if yspd > 0:
                    self.rect.bottom = wall.rect.top
                if yspd < 0:
                    self.rect.top = wall.rect.bottom


    def timewalk(self, vartime, value):
        self.list[vartime] = value

    def enemyattack(self, x, y, px, py, speed):
        self.distx = px - x
        self.disty = py - y
        if self.distx < 0:
            self.move(-speed, 0)
        if self.distx > 0:
            self.move(speed, 0)
        if self.disty > 0:
            self.move(0, speed)
        if self.disty < 0:
            self.move(0, -speed)
    def attack(self):
        if self.dir == "U":
            self.image = pygame.image.load("Imigaes/Player/playerAuraU.png")
        if self.dir == "D":
            self.image = pygame.image.load("Imigaes/Player/playerAuraD.png")
        if self.dir == "L":
            self.image = pygame.image.load("Imigaes/Player/playerAuraL.png")
        if self.dir == "R":
            self.image = pygame.image.load("Imigaes/Player/playerAuraR.png")

class PProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y, d, sprite="Imagaes/Static/static"):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 32, 32)
        self.rect.centerx = x
        self.rect.centery = y
        self.num = 1
        self.image = pygame.image.load(sprite)
        self.d = d
        self.baseimage = sprite
    def homingmissile(self, x, y, px, py, speed):
        self.distx = px - x
        self.disty = py - y
        if self.distx < 0:
            self.move(-speed, 0)
        if self.distx > 0:
            self.move(speed, 0)
        if self.disty > 0:
            self.move(0, speed)
        if self.disty < 0:
            self.move(0, -speed)
    def move(self, spd):
        if self.d == "R":
            self.rect.x += spd
        if self.d == "L":
            self.rect.x -= spd
        if self.d == "D":
            self.rect.y += spd
        if self.d == "U":
            self.rect.y -= spd

    def animate(self, tv , sprite="Imigaes/Static/static"):
        self.baseimage = sprite
        if tv % 4 == 0:
            self.num += 1
            if self.num > 3:
                self.num = 1
        self.image = pygame.image.load(str(self.baseimage)+ str(self.num) + ".png")
