#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gugus
#
# Created:     20/09/2020
# Copyright:   (c) Gugus 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame
import random
pygame.init()



#Variables
fen_width = 1920
fen_height = 1080
fen_size = (fen_width, fen_height)
fen = pygame.display.set_mode(fen_size, pygame.FULLSCREEN)
fen_surface = pygame.display.get_surface()

run = True

TailleX = fen_width // 20
TailleY = fen_height // 20

clock = pygame.time.Clock() #Le nombre d'ips
fps = 30


table = [[0 for j in range(TailleX)] for i in range(TailleY)]

table[10][10] = 1
table[10][11] = 1
table[10][12] = 1
table[10][13] = 1
table[10][14] = 1
table[10][15] = 1
table[11][10] = 1
table[11][11] = 1
table[11][12] = 1
table[11][13] = 1
table[11][14] = 1
table[11][15] = 1



#Fonctions
def draw(fen):
    x = 0
    y = 0
    while y < TailleY:
        while x < TailleX:
            if table[y][x] == 0:
                pygame.draw.rect(fen, (0, 0, 0), (x * 20, y * 20, 20, 20), 1)
            else:
                pygame.draw.rect(fen, (0, 0, 0), (x * 20, y * 20, 20, 20))
            x += 1
        x = 0
        y += 1


def change():
    table2 = [[0 for j in range(TailleX)] for i in range(TailleY)]
    x = 0
    y = 0
    for y in range(TailleY):
        for x in range(TailleX):
            if x > 0:
                left = table[y][x-1]
                if y > 0:
                    left_up = table[y-1][x-1]
                else:
                    left_up = 0
                if y < TailleY - 1:
                    left_down =  table[y+1][x-1]
                else:
                    left_down = 0
            else:
                left = 0
                left_up = 0
                left_down = 0

            if x < TailleX - 1:
                right = table[y][x+1]
                if y > 0:
                    right_up = table[y-1][x+1]
                else:
                    right_up = 0
                if y < TailleY - 1:
                    right_down =  table[y+1][x+1]
                else:
                    right_down = 0
            else:
                right = 0
                right_up = 0
                right_down = 0

            if y > 0:
                up = table[y - 1][x]
            else:
                up = 0

            if y < TailleY - 1:
                down = table[y+1][x]
            else:
                down = 0

            table2[y][x] = up + down + right + right_down + right_up + left + left_down + left_up
        x = 0

    x = 0
    y = 0
    for y in range(TailleY):
        for x in range(TailleX):
            if table2[y][x] == 3 and table[y][x] == 0:
                table[y][x] = 1
            elif table2[y][x] == 2 and table[y][x] == 1:
                table[y][x] = 1
            elif table2[y][x] == 3 and table[y][x] == 1:
                table[y][x] = 1
            else:
                table[y][x] = 0

    return table


#Boucle
while run:
    fen.fill((255, 255, 255))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()
    key2 = pygame.mouse.get_pressed()
    if key[pygame.K_ESCAPE]:
        run = False

    if key[pygame.K_RIGHT]:
        pygame.time.delay(200)
        table = change()

    if key[pygame.K_LEFT]:
        table = change()

    if key[pygame.K_DOWN]:
        table = [[0 for j in range(TailleX)] for i in range(TailleY)]

    if key[pygame.K_UP]:
        for i in range(random.randint(0, (TailleX + TailleY) // 2)):
            table[random.randint(0, TailleY-1)][random.randint(0, TailleX-1)] = 1

    if key2[0] == 1:
        pos = pygame.mouse.get_pos()
        souris = [pos[0]//20, pos[1]//20]
        table[souris[1]][souris[0]] = 1

    if key2[2] == 1:
        pos = pygame.mouse.get_pos()
        souris = [pos[0]//20, pos[1]//20]
        table[souris[1]][souris[0]] = 0


    draw(fen)
    pygame.display.update()

    clock.tick(fps)


pygame.quit()
quit()