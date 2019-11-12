import pygame, time
wgroup = pygame.sprite.Group()


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((x, y), (64, 64))
        self.image = pygame.image.load(sprite)

    def destroy(self):
        self.kill()

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect((x, y), (64, 64))
        self.image = pygame.image.load(sprite)

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite="Imagaes/Static/static"):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 64, 64)
        self.image = pygame.image.load(sprite)
        self.list = []
        self.num = 1
        self.dir = "D"
        for i in range(120):
            self.list.append((x, y))
    def animate(self, tv , sprite="Imigaes/Static/static"):
        if tv % 12 == 0:
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
class PProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y, d, sprite="Imagaes/Static/static"):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 32, 32)
        self.num = 1
        self.image = pygame.image.load(sprite)
        self.d = d
        self.baseimage = sprite
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

