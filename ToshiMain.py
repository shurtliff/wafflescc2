import pygame
import time
import sys
import ToshiC
import KayleC
import ToshiC
import testlevel
import testlevel0
pygame.init()
w = 1920
h = 960
cooldown = 0
clock = pygame.time.Clock()
timeloopclock = 0
screen = pygame.display.set_mode((w,h))
pygame.display.set_mode((w,h))
player = ToshiC.Entity(10, 10, ("Imigaes/Oldguy/oldmanD1.png"))
pewcooldown = 0


playeralive = pygame.sprite.Group()
playeralive.add(player)

Baddies = pygame.sprite.Group()

Allent = pygame.sprite.Group()

Pproj = pygame.sprite.Group()

Breakwall = pygame.sprite.Group()



def createmap(lev):
    ToshiC.wgroup.empty()
    x = y = 0
    for row in lev.map:
        for col in row:
            if col == "W":
                baba = ToshiC.Wall(x, y, "Imigaes/Wall.png")
                ToshiC.wgroup.add(baba)
            if col == "Q":
                baba = ToshiC.Wall(x, y, "Imigaes/Wall.png")
                Breakwall.add(baba)
                ToshiC.wgroup.add(baba)
            if col == "A":
                player.rect.x = x
                player.rect.y = y
            if col == "E":
                Baddies.add(ToshiC.Entity(x, y, "Imigaes/Oldguy/oldmanD2.png"))
            if col == "F":
                fdoor = ToshiC.Wall(x, y, "Imigaes/Wall.png")
                return fdoor
            if col == "B":
                bdoor = ToshiC.Wall(x, y, "Imigaes/Wall.png")
                return bdoor
            x += 64
        y += 64
        x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #-----------------------------------------------------------------------
    pygame.display.flip()
    #-----------------------------------------------------------------------
    collide = pygame.sprite.groupcollide(playeralive, Baddies, 1, 0).keys()
    #-----------------------------------------------------------------------
    if pygame.key.get_pressed()[pygame.K_z]:
        createmap(testlevel)
    if pygame.key.get_pressed()[pygame.K_x]:
        createmap(testlevel0)
    #------------------------------------------------------------------------
    if pygame.key.get_pressed()[pygame.K_w]:
        player.move(0, -2)

    if pygame.key.get_pressed()[pygame.K_s]:
        player.move(0, 2)

    if pygame.key.get_pressed()[pygame.K_a]:
        player.move(-2, 0)

    if pygame.key.get_pressed()[pygame.K_d]:
        player.move(2, 0)

    #-------------------------------------------------------------------------
    if pygame.key.get_pressed()[pygame.K_SPACE] and pewcooldown < 0:
        pewcooldown = 30
        bullet = ToshiC.PProjectile(player.rect.x, player.rect.y, player.dir, "Imigaes/Player/playerattack1.png")
        Pproj.add(bullet)
    pewcooldown -= 1

    #-------------------------------------------------------------------------
    Allent.add(Baddies, playeralive)
    screen.fill((50, 100, 50))
    player.animate(timeloopclock, "Imigaes/Player/Player")
    Allent.draw(screen)
    Pproj.draw(screen)
    ToshiC.wgroup.draw(screen)

    for pew in Pproj:
        pew.animate(timeloopclock, "Imigaes/Player/playerattack")
    for pew in Pproj:
        pew.move(8)
    #Projectile collision
    if pygame.sprite.groupcollide(Pproj, Baddies, 1, 1).keys():
        pass
    if pygame.sprite.groupcollide(Pproj, Breakwall, 1, 1).keys():
        pass
    if pygame.sprite.groupcollide(Pproj, ToshiC.wgroup, 1, 0).keys():
        pass



    #Otherthings
    #------------------------------------------------------

    if timeloopclock < 119:
        timeloopclock = timeloopclock + 1
    else:
        timeloopclock = 0
    if timeloopclock < 118:
        timevalue = timeloopclock + 1
    else:
        timevalue = 0
#saves value into a list to keep track of location of object
    player.timewalk(timeloopclock, (player.rect.x,player.rect.y))
#draw's pillars from the list in DataBasic
#uses the variables to send the player back in time 2 seconds, includes nifty animation too
    cooldown -= 1
    if (pygame.key.get_pressed()[pygame.K_t] or collide) and cooldown < 0:
        playeralive.add(player)
        screen.fill((0, 0, 0))
        cooldown = 240
        for i in range (119):
            if timevalue > 0:
                timevalue = timevalue - 1
            else:
                timevalue = 119
            screen.fill((0, 0, 0))
            player.rect.x = player.list[timevalue][0]
            player.rect.y = player.list[timevalue][1]
            playeralive.draw(screen)
#keeps updating the screen so it doesn't look like chracter is teleoported
            pygame.display.flip()
    clock.tick(60)


