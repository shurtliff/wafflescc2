import pygame
import time
import sys
import AllLevels
import GameC
import GameC
import GameC
import testlevel
import testlevel0
pygame.init()
pygame.mixer.init()

color = (200)
cooldown = 0
babble = True
attack = False

clock = pygame.time.Clock()
timeloopclock = 0
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

player = GameC.Entity(10, 10, ("Imigaes/Player/Player"))
pewcooldown = 0
paused = False
currentlevel = AllLevels.AllLevels[0]



Doorg = pygame.sprite.Group()
Fdoor = pygame.sprite.Group()
Bdoor = pygame.sprite.Group()
playeralive = pygame.sprite.Group()
Baddies = pygame.sprite.Group()
enemy = pygame.sprite.Group()
cbaddy = pygame.sprite.Group()
Allent = pygame.sprite.Group()
Pproj = pygame.sprite.Group()


Breakwall = pygame.sprite.Group()
Key = pygame.sprite.Group()
Ldoor = pygame.sprite.Group()
Chest = pygame.sprite.Group()
Lchest = pygame.sprite.Group()
Mana = pygame.sprite.Group()
Button = pygame.sprite.Group()
Boomywallz = pygame.sprite.Group()
FButton = pygame.sprite.Group()
Boss = pygame.sprite.Group()


selector = 0
playeralive.add(player)
animatecooldown = 0
ready = False


paused = False
currentlevel = AllLevels.AllLevels[0]



def createmap(lev):

    GameC.wgroup.empty()
    Breakwall.empty()
    Fdoor.empty()
    Bdoor.empty()
    Key.empty()
    Ldoor.empty()
    Chest.empty()
    Lchest.empty()
    Mana.empty()
    player.mcharge = 0
    player.kcharge = 0
    Button.empty()
    Boomywallz.empty()
    FButton.empty()
    for a in Baddies:
        a.kill()
    x = 192
    y = 50
    for row in lev:
        for col in row:
            if col == "W":
                baba = GameC.Wall(x, y, "Imigaes/Wall.png")
                GameC.wgroup.add(baba)
            if col == "Q":
                baba = GameC.Wall(x, y, "Imigaes/breakableWall/Bwall1.png")
                Breakwall.add(baba)
                GameC.wgroup.add(baba)
            if col == "A":
                player.rect.x = x
                player.rect.y = y
            if col == "E":
                cbaddy = GameC.Entity(x, y, "Imigaes/BasicEnemy/basicenemy")
                enemy.add(cbaddy)
                Baddies.add(cbaddy)
            if col == "F":
                Fdoor.add(GameC.Wall(x, y, "Imigaes/Door/Door1.png"))
            if col == "B":
                Bdoor.add(GameC.Wall(x, y, "Imigaes/Door/Door4.png"))
            if col == "L":
                Ldoor.add(GameC.Wall(x, y, "Imigaes/Door/Door2.png"))
            if col == "K":
                Key.add(GameC.Wall(x, y, "Imigaes/Static/StaticX2.png"))
            if col == "C":
                Chest.add(GameC.Wall(x, y, "Imigaes/Chest/chest1.png"))
            if col == "m":
                Lchest.add(GameC.Wall(x, y, "Imigaes/Chest/chest1.png"))
            if col == "g":
                Mana.add(GameC.Wall(x, y, "Imigaes/manaorbs/mana", "meow"))
            if col == "O":
                Button.add(GameC.Wall(x, y, "Imigaes/Button/button1.png"))
            if col == "X":
                FButton.add(GameC.Wall(x, y, "Imigaes/Button/button1.png"))
            if col == "J":
                boomwall = GameC.Wall(x, y, "Imigaes/Wall.png")
                Boomywallz.add(boomwall)
                GameC.wgroup.add(boomwall)
            if col == "Y":
                Boss.add(GameC.Wall(x, y, "Imigaes/Button/button1.png", 96, 96))
            x += 64
        y += 64
        x = 192
createmap(AllLevels.AllLevels[0])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pass

    if ready != True:
        wowow = pygame.image.load("Imigaes/titlescreen.png")
        culur = [100, 50, 50]
        screen.fill(culur)
        screen.blit(wowow, (300,190))
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            ready = True
            culur = [100, 50, 50]
            for i in range (25):
                culur[0] -= 4
                culur[1] -= 2
                culur[2] -= 2
                time.sleep(1/25)
                screen.fill(culur)
                screen.blit(wowow, (300,190))
                pygame.display.flip()
            createmap(AllLevels.AllLevels[0])

    if pygame.key.get_pressed()[pygame.K_ESCAPE] and ready == True:
        paused = True
    if paused == True:
        whatwhat = pygame.image.load("Imigaes/escapescreen.png")
        screen.fill((100, 50, 50))
        screen.blit(whatwhat, (500,190))
        if pygame.key.get_pressed()[pygame.K_1]:
            screen.fill((50, 50, 50))
            paused = False
        if pygame.key.get_pressed()[pygame.K_2]:
            createmap(AllLevels.AllLevels[selector])
            screen.fill((0, 0, 0))
            if selector == -1:
                createmap(AllLevels.AllLevels[0])
            else:
                createmap(AllLevels.AllLevels[selector])
            paused = False
        if pygame.key.get_pressed()[pygame.K_3]:
            pygame.quit()
            sys.exit()
    elif ready == True :

#-------------------------------------------------------------------------------------
#Player collides with everything
        collide = pygame.sprite.groupcollide(playeralive, Baddies, 1, 0).keys()
        if pygame.sprite.groupcollide(playeralive, Fdoor, 0, 0).keys():
            selector += 1
            createmap(AllLevels.AllLevels[selector])
            cooldown = 120
        if pygame.sprite.groupcollide(playeralive, Bdoor, 0, 0).keys():
            selector -= 1
            createmap(AllLevels.AllLevels[selector])
            cooldown = 120
        if pygame.sprite.groupcollide(playeralive, Key, 0, 1).keys():
            player.kcharge += 1
        if pygame.sprite.groupcollide(playeralive, Chest, 0, 1).keys():
            pygame.mixer.music.load('Cmagic.mp3')
            pygame.mixer.music.play(0)
            player.mcharge = 3
        if pygame.sprite.groupcollide(playeralive, Button, 0, 1).keys() and player.mcharge > 0:
            player.mcharge -= 1
            animatecooldown = 30
            player.attack()
            for a in Boomywallz:
                a.kill()
        if pygame.sprite.groupcollide(playeralive, FButton, 0, 1).keys() and player.mcharge > 0:
            player.mcharge -= 1
            animatecooldown = 30
            player.attack()
        if pygame.sprite.groupcollide(playeralive, Mana, 0, 1).keys():
            player.mcharge +=1
            if player.mcharge > 3:
                player.mcharge = 3
        for lockedoor in pygame.sprite.groupcollide(playeralive, Ldoor, 0, 0).keys():
            if player.kcharge > 0:
                player.kcharge -= 1
                Fdoor.add(GameC.Wall(lockedoor.rect.x, lockedoor.rect.y, GameC.Entity.animate(timeloopclock, "Imigaes/Door/Door")))
        for lockechest in pygame.sprite.groupcollide(playeralive, Lchest, 0, 0).keys():
            if player.kcharge > 0:
                player.kcharge -= 1
                Chest.add(GameC.Wall(lockechest.rect.x, lockechest.rect.y, "Imigaes/Chest/Chest1.png"))

        for GGOP in enemy:
            GGOP.enemyattack(GGOP.rect.x, GGOP.rect.y, player.rect.x, player.rect.y, 1)
        if animatecooldown > 0:
            attack = True
        if animatecooldown < 0:
            attack = False
        animatecooldown -= 1
        #---------------------------------------------------------------------
#Player moving
        for player in playeralive:
            if pygame.key.get_pressed()[pygame.K_w] and attack == False:
                player.move(0, -4)

            if pygame.key.get_pressed()[pygame.K_s] and attack == False:
                player.move(0, 4)

            if pygame.key.get_pressed()[pygame.K_a] and attack == False:
                player.move(-4, 0)

            if pygame.key.get_pressed()[pygame.K_d] and attack == False:
                player.move(4, 0)

        #-------------------------------------------------------------------------
#Drawing and animation
        Allent.add(Baddies, playeralive)
        screen.fill((50, 50, 50), (192, 50, 1536, 768))
        if attack == False:
            player.animate(timeloopclock, "Imigaes/Player/Player")
        for a in Baddies:
            a.animate(timeloopclock, "Imigaes/BasicEnemy/basicenemy")
        for a in Mana:
            a.animate(timeloopclock, "Imigaes/manaorbs/mana")
        Fdoor.draw(screen)
        Bdoor.draw(screen)
        Allent.draw(screen)
        Pproj.draw(screen)
        Key.draw(screen)
        Ldoor.draw(screen)
        Chest.draw(screen)
        Lchest.draw(screen)
        Mana.draw(screen)
        GameC.wgroup.draw(screen)
        Button.draw(screen)
        Boomywallz.draw(screen)
        FButton.draw(screen)
        #------------------------------------------------------
#pause for attack, fire at the end
        if pygame.key.get_pressed()[pygame.K_SPACE] and pewcooldown < 0 and player.mcharge > 0:
            player.mcharge -= 1
            animatecooldown = 30
            pewcooldown = 30

            player.attack()
        pewcooldown -= 1
        if pewcooldown > 0:
            attack = True
        if pewcooldown == 10:
            pygame.mixer.music.load('Spellsteal.mp3')
            pygame.mixer.music.play(0)
        if pewcooldown == 0:
            bullet = GameC.PProjectile(player.rect.centerx, player.rect.centery, player.dir, "Imigaes/Player/playerattack1.png")
            Pproj.add(bullet)


        if pewcooldown < 0:
            attack = False

        #-------------------------------------------------------------------------
#Projectile physics
        for pew in Pproj:
            pew.animate(timeloopclock, "Imigaes/Player/playerattack")
        for pew in Pproj:
            pew.move(8)
        if pygame.sprite.groupcollide(Pproj, Baddies, 1, 1).keys():
            pygame.mixer.music.load('Fizzle.mp3')
            pygame.mixer.music.play(0)

        if pygame.sprite.groupcollide(Pproj, Breakwall, 1, 1).keys():
            pygame.mixer.music.load('Bam.mp3')
            pygame.mixer.music.play(0)

        if pygame.sprite.groupcollide(Pproj, GameC.wgroup, 1, 0).keys():
            pygame.mixer.music.load('Bam.mp3')
            pygame.mixer.music.play(0)



        screen.fill((0, 0, 0), (192, 818,1536,64))
        if player.mcharge > 0:
            orbies = pygame.image.load("Imigaes/manaorbs/mana2.png")
            screen.blit(orbies, (192, 818))
        if player.mcharge > 1:
            orbies = pygame.image.load("Imigaes/manaorbs/mana3.png")
            screen.blit(orbies, (256, 818))
        if player.mcharge > 2:
            orbies = pygame.image.load("Imigaes/manaorbs/mana1.png")
            screen.blit(orbies, (320, 818))



        #--------------------------------------------------------------------------

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
        if (pygame.key.get_pressed()[pygame.K_t] or collide) and cooldown < 0 and babble:
            pygame.mixer.music.load('Rewinds.mp3')
            pygame.mixer.music.play(0)
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
    if player.alive() == False:
        babble = False
        if color != 0:
            wowow = pygame.image.load("Imigaes/Rewind.png")
            wowow1 = pygame.image.load("Imigaes/Yes.png")
            wowow2 = pygame.image.load("Imigaes/No.png")
            baby = [color, color, color]
            screen.fill(baby)
            color -= 5
        if color == 0:
            screen.fill(baby)
            screen.blit(wowow, (610,100))
            screen.blit(wowow1, (110,700))
            screen.blit(wowow2, (1110,700))
            if pygame.key.get_pressed()[pygame.K_y]:
                color = 0
                for i in range(17):
                    baby = [color, color, color]
                    screen.fill(baby)
                    pygame.display.flip()
                    color += 15
                    time.sleep(1/17)
                    if selector == -1:
                        createmap(AllLevels.AllLevels[0])
                    else:
                        createmap(AllLevels.AllLevels[selector])
                playeralive.add(player)
                babble = True
                screen.fill([0, 0, 0])
            if pygame.key.get_pressed()[pygame.K_n]:
                color = 0
                kentucky = pygame.image.load("Imigaes/Endingscreen.png")
                for i in range(17):
                    baby = [color, color, color]
                    screen.fill(baby)
                    pygame.display.flip()
                    color += 15
                    time.sleep(1/17)
                screen.blit(kentucky, (0,0))
                pygame.display.flip()
                time.sleep(10)

                pygame.quit()
                sys.exit()

    clock.tick(60)

    #-----------------------------------------------------------------------
    pygame.display.flip()
    #-----------------------------------------------------------------------
