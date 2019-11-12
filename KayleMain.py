import pygame
import time
import sys
import AllLevels
import KayleC
import KayleC
import ToshiC
import testlevel
import testlevel0
pygame.init()
import StartScreen
w = 1920
h = 960

cooldown = 0
newmap = 0
clock = pygame.time.Clock()
timeloopclock = 0
screen = pygame.display.set_mode((w,h))
pygame.display.set_mode((w,h))
player = KayleC.Entity(10, 10, ("Imigaes/Static/staticC1.png"))

Doorg = pygame.sprite.Group()

playeralive = pygame.sprite.Group()
playeralive.add(player)

Baddies = pygame.sprite.Group()

Allent = pygame.sprite.Group()

currentlevel = StartScreen.map




def createmap(lev):
    KayleC.wgroup.empty()
    Doorg.empty()
    x = y = 0
    select = 0
    for row in lev:
        for col in row:
            if col == "W":
                baba = KayleC.Wall(x, y, "Imigaes/Wall.png")
                KayleC.wgroup.add(baba)
            if col == "A":
                player.rect.x = x
                player.rect.y = y
            if col == "E":
                Baddies.add(KayleC.Entity(x, y, "Imigaes/Oldguy/oldmanD2.png"))
            if col == "D":
                Door = KayleC.Door(x, y, select, "Imigaes/Door/Door1.png")
                Doorg.add(Door)
                select += 1
                print(select)

            x += 64
        y += 64
        x = 0
createmap(StartScreen.map)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    smackadoor = pygame.sprite.spritecollide(player, Doorg, False)
    for door in smackadoor:
        door.animate(timeloopclock, "Imigaes/Door/Door")
        createmap(AllLevels.AllLevels[door.id])

    #-----------------------------------------------------------------------
    pygame.display.flip()
    #-----------------------------------------------------------------------
    collide = pygame.sprite.groupcollide(playeralive, Baddies, 1, 0).keys()

    #---------------------------------------------------------------------
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
    Allent.add(Baddies, playeralive)
    screen.fill((50, 50, 50))
    player.animate(timeloopclock, "Imigaes/Player/Player")
    Allent.draw(screen)
    Doorg.draw(screen)
    #------------------------------------------------------
    KayleC.wgroup.draw(screen)
    KayleC.dgroup.draw(screen)
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


