#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ashad
#
# Created:     20-05-2019
# Copyright:   (c) ashad 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pygame import *
from random import *
running = True
screen = display.set_mode((800,600))
vx = 10
vy = 0
shotX = 100
bShotX = 600
laserpic = image.load("laser.jpg")
laser = transform.scale(laserpic,(20,10))
laserpic2 = image.load("laser2.jpg")
laser2 = transform.scale(laserpic2,(20,10))
clock = time.Clock()
timer = 0
progress = 0
shots = []
shooter = Rect(100,300,40,40)
shotbox = Rect(shooter.x,300,21,11)

bossRect = Rect(600,200,200,200)
bossHP = 10
userHP = 5
red = (255,0,0)
white = (255,255,255)
screen.fill((white))
randposes = []

randpos = randint(200,400)
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

    p = key.get_pressed()
    timer += 1
    progress = timer/60

    if p[K_UP]:
        shots = ['shot']
        shotY = shooter.y
        


    print(randpos)

    bShotbox = Rect(bShotX-11,randpos,22,11)
    bHitbox = bShotbox.move(bShotX-610,randpos)
    #screen.fill(white)



    screen.fill(white)
    draw.rect(screen,red,bossRect)
    bShotX -= 10
    draw.rect(screen,(0,0,0),bShotbox,1)
    screen.blit(laser2,(bShotX,randpos))

    if bShotX < 135:
        bShotX = 600
        randpos = (randint(200,400))
    if bShotbox.colliderect(shooter):
        userHP -= 1
        bShot = 600
    if len(shots)==1:
        shotX += vx
        draw.rect(screen,red,bossRect)
        hitbox = shotbox.move((shotX-100,0))
        screen.blit(laser,(shotX,shotY))
        draw.rect(screen,(0,0,0),hitbox,1)
        if hitbox.colliderect(bossRect):
            bossHP -= 1
            shotX = 100
            shots = []
            print(bossHP)
        if shotX > 700:
            shotX = 100
            shots.remove('shot')

    if bossHP == 0:
        runnning = False
    if userHP == 0:
        running = False
    print(bossHP,userHP)
   # print(bShotX)
    #moveguy
    if p[K_SPACE]:
        vy = -10
    shooter.y += vy
   # screen.fill(white)
    draw.rect(screen,red,(shooter.x,shooter.y,40,40))
    if shooter.y >= 300:
        shooter.y = 300
        vy = 0
    vy += 1


    clock.tick(60)
    display.flip()
quit()
