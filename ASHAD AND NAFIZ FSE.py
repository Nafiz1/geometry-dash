#Ashad Ahmed & Nafiz Hasan
#ASHAD AND NAFIZ FSE.py
#This program is a replica of the game Geometry Dash. However, it has some extra
#features such as a boss level and barrier blocks. It has things that are in the
#original game too, such as a store, spikes, double jump blocks, etc. There are
#three levels, each with its own difficulty and design, with the designs made
#entirely by us using masks and text files.

from pygame import *
from random import *

#guy variables
X=0
Y=1
VY=2
jumping=3
score=4
progress = 5
page = 6
angle = 7
previouspg = 8
shotX = 9
finalscore = 10
power = 11
shotY = 12

#store variables
buy2 = 0
buy3 = 1

#boss variables
bossHP = 0
drawingBoss = 1
bosstime = 2
bShotX = 3
bossbeat = 4

init()

screen = display.set_mode((800,600))
display.set_caption("Geometry Dash")

#importing

song3 = mixer.Sound("song3.wav")
song2 = mixer.Sound("song2.wav")
song1 = mixer.Sound("song1.wav")
die = mixer.Sound("explode_11.wav")

#lvl1
backPic = image.load("Geobackgroundlvl1mask.png")
platformMask = image.load("masklvl1.png")
wallMask = image.load("wallmasklvl1.png")
#lvl2
backPic2 = image.load("GeoBackground2.png")
platformMask2 = image.load("masklvl2.png")
wallMask2 = image.load("wallmasklvl2.png")
#lvl3
backPic3 = image.load("Geobackgroundlevel3.png")
platformMask3 = image.load("masklevel3.png")
wallMask3 = image.load("wallmasklevel3.png")
#pics
breakblockPictransform = image.load("BrickBlock.png")
breakblockPic = transform.scale(breakblockPictransform,(20,250))
character = image.load("character.png")
guyPic = transform.scale(character,(30,30))
menuback = image.load("menubackground.png")
menubackground = transform.scale(menuback,(800,600))
title = image.load("geotitle.png")
geotitle = transform.scale(title,(300,50))
laserpic = image.load("laser.jpg")
laser = transform.scale(laserpic,(20,10))
lvlcom = image.load("lvlcom.png")
spikePictransform = image.load("spike.png")
spikePic = transform.scale(spikePictransform,(20,30))
spikePictransform2 = image.load("spikedown.png")
spikePic2 = transform.scale(spikePictransform2,(20,30))
coinPictransform = image.load("coin.png")
coinPic = transform.scale(coinPictransform,(20,20))
instructionsPic = image.load("instructions.jpg")
instructions = transform.scale(instructionsPic,(800,600))
creditsPic = image.load("credits.jpg")
creditss = transform.scale(creditsPic,(800,600))
storePic = image.load("storefront.jpg")
store = transform.scale(storePic,(800,600))
character2Pic = image.load("character2.png")
character2 = transform.scale(character2Pic,(30,30))
character3Pic = image.load("character3.png")
character3 = transform.scale(character3Pic,(30,30))
twentyfivegoldPic = image.load("25gold.png")
twentyfivegold = transform.scale(twentyfivegoldPic,(100,50))
fiftygoldPic = image.load("50gold.png")
fiftygold = transform.scale(fiftygoldPic,(100,50))
greenpoweruptransform = image.load("greenpowerup.png")
greenpowerup = transform.scale(greenpoweruptransform,(20,20))
redpoweruptransform = image.load("redpowerup.png")
redpowerup = transform.scale(redpoweruptransform,(20,20))
yellowringtransform = image.load("YellowRing.png")
yellowring = transform.scale(yellowringtransform,(30,30))
magentaringtransform = image.load("MagentaRing.png")
magentaring = transform.scale(magentaringtransform,(30,30))
laserPictransform = image.load("laser.png")
laserPic = transform.scale(laserPictransform,(30,20))
fireballPic = image.load("fireball.jpg")
fireball = transform.scale(fireballPic,(30,30))
evildashPic = image.load("evildash.jpg")
evildash = transform.scale(evildashPic,(200,200))
playPic = image.load("play.png")
play = transform.scale(playPic,(150,50))
instructionsButtonPic = image.load("instructionsbutton.png")
instructionsButton = transform.scale(instructionsButtonPic,(200,50))
storeButtonPic = image.load("store.png")
storeButton = transform.scale(storeButtonPic,(150,50))
creditsbuttonPic = image.load("creditsbutton.png")
creditsButton = transform.scale(creditsbuttonPic,(150,50))
backbuttonPic = image.load("back.png")
backbutton = transform.scale(backbuttonPic,(120,50))
resumebuttonPic = image.load("resumebutton.png")
resumebutton = transform.scale(resumebuttonPic,(150,50))
restartbuttonPic = image.load("restartbutton.png")
restartButton = transform.scale(restartbuttonPic,(150,50))
lvl1prePic = image.load("lvl1pre.jpg")
lvl1pre = transform.scale(lvl1prePic,(150,150))
lvl2prePic = image.load("lvl2pre.jpg")
lvl2pre = transform.scale(lvl2prePic,(150,150))
lvl3prePic = image.load("lvl3pre.jpg")
lvl3pre = transform.scale(lvl3prePic,(150,150))
gamePic = image.load("game.png")
game = transform.scale(gamePic,(200,50))
pausePic = image.load("paused.png")
pause = transform.scale(pausePic,(200,50))
soldtransform = image.load("sold.png")
sold = transform.scale(soldtransform,(100,100))
lvl1wordPic = image.load("lvl1word.png")
lvl1word = transform.scale(lvl1wordPic,(100,50))
lvl2wordPic = image.load("lvl2word.png")
lvl2word = transform.scale(lvl2wordPic,(100,50))
lvl3wordPic = image.load("lvl3word.png")
lvl3word = transform.scale(lvl3wordPic,(100,50))

spikepos = open("spikeslvl1.txt").read().strip().replace(",","\n").split()
spikepos2 = open("spikes.txt").read().strip().replace(",","\n").split()
spikepos3 = open("spikes3.txt").read().strip().replace(",","\n").split()
upsidepos = open("spikeslvl1upsidedown.txt").read().strip().replace(",","\n").split()
upsidepos2 = open("upsidespikes.txt").read().strip().replace(",","\n").split()
coinposlvl2 = open("coins.txt").read().strip().replace(",","\n").split()
coinposlvl1 = open("coinslvl1coords.txt").read().strip().replace(",","\n").split()
coinposlvl3 = open("coinslvl3coords.txt").read().strip().replace(",","\n").split()
bblockpos = open("breakblocks.txt").read().strip().replace(",","\n").split()
jblockpos = open("jumpblocks.txt").read().strip().replace(",","\n").split()

darkblue = (30,144,255)
red = (255,0,0)
white = (255,255,255)
shots = []
randpos = randint(308,478)
display.set_icon(guyPic)
shots = []

def menu(guy,screen,page):
    global guyPic
    keys = key.get_pressed()
    
    if guy[page] == "menu":
        screen.blit(menubackground,(0,0))
        screen.blit(geotitle,(225,50))
        screenGuy = transform.scale(guyPic,(100,100))
        screenGuy2 = transform.rotate(screenGuy,40)
        screen.blit(screenGuy2,(50,200))
        screenSpike = transform.scale(spikePic,(50,50))
        screen.blit(screenSpike,(160,330))
        buttons = [draw.rect(screen,darkblue,(300,150,150,50)),draw.rect(screen,darkblue,(275,250,200,50)),draw.rect(screen,darkblue,(300,350,150,50)),draw.rect(screen,darkblue,(300,450,150,50))]
        screen.blit(play,(300,150))
        screen.blit(instructionsButton,(275,250))
        screen.blit(storeButton,(300,350))
        screen.blit(creditsButton,(300,450))
        if buttons[0].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(300,150,150,50),1)
        if buttons[1].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(275,250,200,50),1)
        if buttons[2].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(300,350,150,50),1)
        if buttons[3].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(300,450,150,50),1)
        if click and buttons[0].collidepoint(mx,my):
            guy[page] = "select"
        if click and buttons[1].collidepoint(mx,my):
            guy[page] = "instructions"
        if click and buttons[2].collidepoint(mx,my):
            guy[page] = "store"
        if click and buttons[3].collidepoint(mx,my):
            guy[page] = "credits"

    if guy[page] == "store":
        screen.blit(store,(0,0))
        ch2Rect = Rect(150,300,30,30)
        ch3Rect = Rect(400,300,30,30)
        s2Rect = Rect(120,325,100,50)
        s3Rect = Rect(370,325,100,50)
        if storelist[buy2] == 0:
            screen.blit(sold,s2Rect)
        if storelist[buy3] == 0:
            screen.blit(sold,s3Rect)
        screen.blit(character2,ch2Rect)
        screen.blit(character3,ch3Rect)
        screen.blit(twentyfivegold,(120,350))
        screen.blit(fiftygold,(370,350))
        backRect = Rect(580,440,120,50)
        draw.rect(screen,red,backRect)
        screen.blit(backbutton,(580,440))
        
        if backRect.collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(580,440,120,50),1)
        if click and backRect.collidepoint(mx,my):
            guy[page] = "menu"
        if click and ch2Rect.collidepoint(mx,my):
            if guy[finalscore] >= storelist[buy2]:
                guyPic = character2
                guy[finalscore] = guy[finalscore] - storelist[buy2]
                storelist[buy2] = 0
        if click and ch3Rect.collidepoint(mx,my):
            if guy[finalscore] >= storelist[buy3]:
                guyPic = character3
                guy[finalscore] = guy[finalscore] - storelist[buy3]
                storelist[buy3] = 0
    
    if guy[page] == "credits":
        screen.blit(creditss,(0,0))
        backkey = draw.rect(screen,red,(350,500,120,50))
        screen.blit(backbutton,(350,500))
        if backkey.collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(350,500,120,50),1)
        if click and backkey.collidepoint(mx,my):
            guy[page] = "menu"
            
    if guy[page] == "select":
        screen.blit(menubackground,(0,0))
        screen.blit(geotitle,(225,50))
        levels = [draw.rect(screen,(255,0,0),(130,200,150,150)),draw.rect(screen,(255,0,0),(330,200,150,150)),draw.rect(screen,(255,0,0),(530,200,150,150))]
        screen.blit(lvl1pre,(130,200))
        screen.blit(lvl2pre,(330,200))
        screen.blit(lvl3pre,(530,200))
        screen.blit(lvl1word,(155,355))
        screen.blit(lvl2word,(355,355))
        screen.blit(lvl3word,(555,355))
        
        if levels[0].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(130,200,150,150),1)
        if levels[1].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(330,200,150,150),1)
        if levels[2].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(530,200,150,150),1)
            
        if click and levels[0].collidepoint(mx,my):
            guy[page]="lvl1"
            guy[previouspg] = "lvl1"
        if click and levels[1].collidepoint(mx,my):
            guy[page]="lvl2"
            guy[previouspg] = "lvl2"
        if click and levels[2].collidepoint(mx,my):
            guy[page]="lvl3"
            guy[previouspg] = "lvl3"
            
        back = draw.rect(screen,red,(350,450,120,50))
        screen.blit(backbutton,(350,450))
        if back.collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(350,450,120,50),1)
        if click and back.collidepoint(mx,my):
            guy[page] = "menu"
            
    if keys[K_ESCAPE] and guy[page] == "lvl1":
        guy[page] = "ingamemenu"
    if keys[K_ESCAPE] and guy[page] == "lvl2":
        guy[page] = "ingamemenu"
    if keys[K_ESCAPE] and guy[page] == "lvl3":
        guy[page] = "ingamemenu"
        
    if guy[page] == "ingamemenu":
        screen.blit(menubackground,(0,0))
        options = [draw.rect(screen,red,(300,50,150,50)),draw.rect(screen,red,(300,200,150,50)),draw.rect(screen,red,(275,350,200,50)),draw.rect(screen,red,(300,500,150,50))]

        screen.blit(resumebutton,(300,50))
        screen.blit(backbutton,(315,200))
        screen.blit(instructionsButton,(275,350))
        screen.blit(restartButton,(300,500))
        screen.blit(game,(50,200))
        screen.blit(pause,(500,470))
        screenGuy = transform.scale(guyPic,(50,50))
        screenGuy2 = transform.rotate(screenGuy,-40)
        screen.blit(screenGuy2,(600,100))

        if options[0].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(300,50,150,50),1)
        if options[1].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(300,200,150,50),1)
        if options[2].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(275,350,200,50),1)
        if options[3].collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(300,500,150,50),1)
            
        if click and options[0].collidepoint(mx,my):
            guy[page] = guy[previouspg]
            
        if click and options[1].collidepoint(mx,my):
            guy[page] = "select"
            if guy[previouspg] == "lvl1":
                for i in range(len(drawing)):
                    drawing[i] = True
            if guy[previouspg] == "lvl2":
                for i in range(len(drawing2)):
                    drawing2[i] = True
            if guy[previouspg] == "lvl3":
                for i in range(len(drawing3)):
                    drawing3[i] = True
            if guy[previouspg] == "lvl3":
                for i in range(len(bbdrawing)):
                    bbdrawing[i] = True
                    
            guy[angle] = 0
            guy[X] = 250
            guy[Y] = 478
            guy[score] = 0
            guy[progress] = 0
            guy[power] = False
            
        if click and options[2].collidepoint(mx,my):
            guy[page] = "instructions2"
        if click and options[3].collidepoint(mx,my):
            guy[page] = guy[previouspg]
            guy[X] = 250
            if guy[previouspg] == "lvl1":
                for i in range(len(drawing)):
                    drawing[i] = True
            if guy[previouspg] == "lvl2":
                for i in range(len(drawing2)):
                    drawing2[i] = True
            if guy[previouspg] == "lvl3":
                for i in range(len(drawing3)):
                    drawing3[i] = True
            guy[angle] = 0
            guy[X] = 250
            guy[Y] = 478
            guy[score] = 0
            guy[progress] = 0
            guy[power] = False
    
    if guy[page] == "instructions":
        screen.blit(instructions,(0,0))
        backkey = draw.rect(screen,red,(340,500,120,50))
        screen.blit(backbutton,(340,500))
        if backkey.collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(340,500,120,50),1)
        if click and backkey.collidepoint(mx,my):
            guy[page] = "menu"
            
    if guy[page] == "instructions2":
        screen.blit(instructions,(0,0))
        backkey = draw.rect(screen,red,(340,470,120,50))
        screen.blit(backbutton,(340,470))
        if backkey.collidepoint(mx,my):
            draw.rect(screen,(0,0,0),(340,470,120,50),1)
        if click and backkey.collidepoint(mx,my):
            guy[page] = "ingamemenu"  
                
def drawScene(screen,guy,drawing):
    offset = 250-guy[X]
    hitbox = Rect(guy[X]+20,guy[Y],1,31)
    h = hitbox.move(offset,0)
    keys = key.get_pressed()

    if guy[page] == "lvl1":
        screen.blit(backPic, (offset,0))
        
        draw.rect(screen,(0,0,0),(325,20,118,15),1)
        draw.rect(screen,(0,255,0),(327,20,guy[progress],13))
        
        #upsidedown spikes
        for us in upsidespikes:
            u = us.move(offset,0)
            screen.blit(spikePic2,u)
        #rightsideup spikes
        for ss in spikes:
            s = ss.move(offset,0)
            screen.blit(spikePic,s)
            
        for coin in range(len(coins)):
            c = coins[coin].move(offset,0)
            if drawing[coin] == True:
                screen.blit(coinPic,c)
            if h.colliderect(c):
                guy[score] += 1
                drawing[coin] = False

    if guy[page] == "lvl2":
        screen.blit(backPic2, (offset,0)) #moving the background

        draw.line(screen,(0,0,0),(0,509),(10000,509),1) #ground line

        #progress bar
        draw.rect(screen,(0,0,0),(325,20,135,15),1)
        draw.rect(screen,(0,255,0),(327,20,guy[progress],13))

        #hitbox for collecting coins
        hitbox2 = Rect(guy[X]+20,guy[Y],1,31)
        h2 = hitbox2.move(offset,0)

        for spike in spikes2: #drawing spikes
            s = spike.move(offset,0)
            screen.blit(spikePic,s)

        for coin in range(len(coins2)): #drawing coins
            c = coins2[coin].move(offset,0)
            if drawing2[coin] == True:
                screen.blit(coinPic,c)
            if h2.colliderect(c):
                guy[score] += 1
                drawing2[coin] = False

    if guy[page] == "lvl3":
        screen.blit(backPic3, (offset,0)) #moving the background

        draw.rect(screen,(0,0,0),(325,20,125,15),1)
        draw.rect(screen,(0,255,0),(327,21,guy[progress],13))
        
        draw.line(screen,(0,0,0),(0,509),(10000,509),1) #ground line

        hitbox3 = Rect(guy[X],guy[Y],35,35) 
        h3 = hitbox.move(offset,0) #hitbox for jumpblocks

        #drawing spikes
        for spike in spikes3:
            s = spike.move(offset,0)
            screen.blit(spikePic,s)

        for us2 in upsidespikes2:
            u2 = us2.move(offset,0)
            screen.blit(spikePic2,u2)

        for coin in range(len(coins3)):
            c = coins3[coin].move(offset,0)
            if drawing3[coin] == True:
                screen.blit(coinPic,c)
            if h.colliderect(c):
                guy[score] += 1
                drawing3[coin] = False

        #drawing jumpblocks
        for jbs in jumpblocks:
            j = jbs.move(offset,0)
            if h3.colliderect(j): #if guy is on jumpblock, he can jump again
                guy[jumping] = False
                screen.blit(magentaring,j)
            else:
                screen.blit(yellowring,j)

        #if guy picks up powerup
        p = powerup.move(offset,0)
        screen.blit(redpowerup,p)
        if guy[power] == True:
            screen.blit(greenpowerup,p)

        #drawing breakable blocks
        for bblock in range(len(breakblocks)):
            b = breakblocks[bblock].move(offset,0)
            if bbdrawing[bblock] == True:
                screen.blit(breakblockPic,b)
                if h3.colliderect(b):
                    for i in range(len(bbdrawing)):
                        bbdrawing[i] = True
                    for i in range(len(drawing3)):
                        drawing3[i] = True
                    #resetting everything
                    guy[Y] = 478 #I know we should have made a reset function
                    guy[X] = 250 #instead of copy and pasting it multiple times,
                    guy[shotX] = 250 #but it was too late but the time we realized
                    guy[score] = 0
                    guy[progress] = 0
                    guy[power] = False

                    guy[shotY] = guy[Y]
                    die.play(0)
                    time.wait(300)

        #----------------------------------------------------
        #shooting
        keys = key.get_pressed()
        global shots
        global shothitbox
        if guy[power] == True:
            if keys[K_UP]:
                shots = ['shot']
                if guy[shotX] == 250:
                    guy[shotY] = guy[Y]

            if len(shots)==1:
                guy[shotX]+=10

                shothitbox = Rect(guy[shotX],guy[shotY],20,10)
                screen.blit(laserPic,(guy[shotX],guy[shotY]))
                
                for bblock in range(len(breakblocks)):
                    b = breakblocks[bblock].move(offset,0)
                    if shothitbox.colliderect(b):
                        bbdrawing[bblock] = False
            
            if guy[shotX] > 700:
                guy[shotX] = 250
                shots.remove('shot')
        #-----------------------------------------------------   
        #boss
        global bossRect
        global boss
        global bossHP
        global bShotX
        global randpos
        global drawingBoss
        global bosstime

        shothitbox = Rect(guy[shotX],guy[shotY],20,10)
        bshothitbox = Rect(bosslist[bShotX],randpos,20,10)
        
        if guy[X] < 12600 and bosslist[drawingBoss] == True:
            bossRect = Rect(13000,308,200,200)
            boss = bossRect.move(offset,0)
            screen.blit(evildash,boss)
        
        if guy[X] >12600 and bosslist[drawingBoss] == True:
            guy[power] = True
            bossRect = Rect(guy[X]+400,308,200,200)
            boss = bossRect.move(offset,0)
            screen.blit(evildash,boss)
            bosslist[bShotX] -= 10
            if bosslist[bShotX] < 135:
                bosslist[bShotX] = 600
                randpos = randint(308,478)
            screen.blit(fireball,(bosslist[bShotX],randpos))
            bossTimer(guy)
            if bshothitbox.colliderect(h):
                guy[X] = 250
                bosslist[bossHP] = 30
                guy[X] = 250
                guy[Y] = 478
                guy[score] = 0
                guy[progress] = 0
                for i in range(len(drawing3)):
                    drawing3[i] = True
                for i in range(len(bbdrawing)):
                    bbdrawing[i] = True
                guy[power] = False
                guy[shotY] = guy[Y]
            
        if bosslist[bosstime] <= 0:
            bosslist[bossHP] = 30
            guy[X] = 250
            guy[Y] = 478
            guy[score] = 0
            guy[progress] = 0
            guy[angle] = 0
            for i in range(len(drawing3)):
                drawing3[i] = True
            for i in range(len(bbdrawing)):
                bbdrawing[i] = True
            bosslist[bosstime] = 8
            guy[shotY] = guy[Y]
            guy[power] = False
            
        if shothitbox.colliderect(boss):
            bosslist[bossHP] -=1
            
        if bosslist[bossHP] < 0:
            bosslist[drawingBoss] = False
            bosslist[bossbeat] = True
        #-----------------------------------------------------
                
    rotatepic = transform.rotate(guyPic,guy[angle])
    screen.blit(rotatepic, (250,guy[Y]))
    
def bossTimer(guy):
    global bosstime
    if guy[page] == "lvl3":
        font.init()
        timesFont = font.SysFont("Times New Roman", 20)
        txt = timesFont.render("TIME LEFT: %s" % int(bosslist[bosstime]), True, (255,0,0))
        screen.blit(txt,(100,530))
        font.quit()
        del timesFont
        if bosslist[bosstime] > 0:
            bosslist[bosstime]-=1/60
            
def move(guy):
    if guy[page] == "lvl1":
        if guy[X] <= 14501:
            guy[X] += 1
        elif guy[X] >= 14502:
            guy[X] += 0
    if guy[page] == "lvl2":
        if guy[X] < 15401:
            guy[X] += 1
    if bosslist[bossHP] >0:
        if guy[X] < 15401:
            guy[X] += 6
            
def jump(guy):
    if guy[page] == "lvl1":
        keys = key.get_pressed()
        
        if keys[K_SPACE] and guy[jumping]==False:
            guy[VY] = -14
            guy[jumping]=True

        guy[Y]+=guy[VY]
        #if guy is on ground stop jumping
        if guy[Y] >= 478:
            guy[Y] = 478
            guy[VY] = 0
            guy[jumping]=False
        guy[VY]+= 1
        
    if guy[page] == "lvl2":
        keys = key.get_pressed()
        
        if keys[K_SPACE] and guy[jumping]==False:
            guy[VY] = -12
            guy[jumping]=True

        guy[Y]+=guy[VY]
        #if guy is on ground stop jumping
        if guy[Y] >= 478:
            guy[Y] = 478
            guy[VY] = 0
            guy[jumping]=False
        guy[VY]+= 1
            
    if guy[page] == "lvl3":
        keys = key.get_pressed()
        
        if guy[X] <8000 or guy[X] >12500:
            if keys[K_SPACE] and guy[jumping]==False:
                guy[VY] = -13
                guy[jumping]=True
            guy[Y]+=guy[VY]
            if guy[Y] >= 478:
                guy[Y] = 478
                guy[VY] = 0
                guy[jumping]=False
            guy[VY]+= 1

def upsidedownjump(guy):
    keys = key.get_pressed()
    hitbox = Rect(guy[X],guy[Y],30,30)
    
    if keys[K_SPACE] and guy[jumping]==False:
        guy[VY] += 13
        guy[jumping]=True

    guy[Y]+=guy[VY]
    if guy[Y] <= 0:
        guy[Y] = 0
        guy[VY] = 0
        guy[jumping]=False
    guy[VY] -= 1

def clearPlatforms(guy):
    if platformMask.get_at((guy[X],guy[Y])) != platforms:
        return True #if it doesnt hit platform
    else:
        return False #if it does
    
def clearPlatforms2(guy):
    if platformMask2.get_at((guy[X],guy[Y])) != platforms:
        return True 
    else:
        return False 

def clearPlatforms3(guy):
    if platformMask3.get_at((guy[X],guy[Y])) != platforms:
        return True
    else:
        return False

def clearWalls(guy):
    if wallMask.get_at((guy[X],guy[Y])) != walls:
        return True #if it doesnt hit wall
    else:
        return False #if it does
    
def clearWalls2(guy):
    if wallMask2.get_at((guy[X],guy[Y])) != walls:
        return True
    else:
        return False
    
def clearWalls3(guy):
    if wallMask3.get_at((guy[X],guy[Y])) != walls:
        return True
    else:
        return False

def checkPlatforms(guy,platforms):
    if guy[page] == "lvl1":
        if guy[VY]>0 and clearPlatforms((guy[X]+29,guy[Y]+36))==False:
            guy[jumping]=False
            guy[VY] = 0
    if guy[page] == "lvl2":
        if guy[VY]>0 and clearPlatforms2((guy[X]+29,guy[Y]+36))==False: #if guy is hitting a platform
            guy[jumping]=False
            guy[VY] = 0
    if guy[page] == "lvl3":
        if guy[X] <8000 or guy[X] >12500:
            if guy[VY]>0 and clearPlatforms3((guy[X]+29,guy[Y]+36))==False:
                guy[jumping]=False
                guy[VY] = 0
        else:
            if guy[VY]<0 and clearPlatforms3((guy[X]+29,guy[Y]))==False:
                guy[jumping]=False
                guy[VY] = 0

def checkWalls(guy,walls):
    if guy[page] == "lvl1":
        if clearWalls((guy[X]+29,guy[Y]+32))==False:
            print("die")
            #if guy dies, reset everything
            for i in range(len(drawing)):
                drawing[i] = True
            guy[angle] = 0
            guy[X] = 250
            guy[Y] = 478
            guy[score] = 0
            guy[progress] = 0
            guy[power] = False
            die.play(0)
            time.wait(300)
    if guy[page] == "lvl2":
        if clearWalls2((guy[X]+29,guy[Y]+32))==False:
            print("die")
            for i in range(len(drawing2)):
                drawing2[i] = True
            guy[angle] = 0
            guy[X] = 250
            guy[Y] = 478
            guy[score] = 0
            guy[progress] = 0
            guy[power] = False
            mixer.find_channel().play(die,0)
            time.wait(300)
    if guy[page] == "lvl3":  
        if clearWalls3((guy[X]+29,guy[Y]+36))==False:
            print("die")
            for i in range(len(drawing3)):
                drawing3[i] = True
            guy[angle] = 0
            guy[X] = 250
            guy[Y] = 478
            guy[score] = 0
            guy[progress] = 0
            guy[power] = False
            guy[shotY] = guy[Y]
            die.play(0)

def checkSpikes(guy,spikes,spikes2,spikes3):
    hitbox = Rect(guy[X],guy[Y],29,31)
    
    if guy[page] == "lvl1":
        for s in spikes:
            if hitbox.colliderect(s):
                for i in range(len(drawing)):
                    drawing[i] = True
                guy[angle] = 0
                guy[X] = 250
                guy[Y] = 478
                guy[score] = 0
                guy[progress] = 0
                die.play(0)
                time.wait(300)
                
        for us in upsidespikes:
            if hitbox.colliderect(us):
                for i in range(len(drawing)):
                    drawing[i] = True
                guy[angle] = 0
                guy[X] = 250
                guy[Y] = 478
                guy[score] = 0
                guy[progress] = 0
                die.play(0)
                time.wait(300)
                
    if guy[page] == "lvl2":
        for s in spikes2:
            if hitbox.colliderect(s):
                for i in range(len(drawing2)):
                    drawing2[i] = True
                guy[angle] = 0
                guy[X] = 250
                guy[Y] = 478
                guy[score] = 0
                guy[progress] = 0
                die.play(0)
                time.wait(300)
                
    if guy[page] == "lvl3":
        for s in spikes3:
            if hitbox.colliderect(s):
                for i in range(len(drawing3)):
                    drawing3[i] = True
                for i in range(len(bbdrawing)):
                    bbdrawing[i] = True
                guy[angle] = 0
                guy[X] = 250
                guy[Y] = 478
                guy[score] = 0
                guy[power] = False
                guy[shotY] = guy[Y]
                die.play(0)
                time.wait(300)

        for us2 in upsidespikes2:
            if hitbox.colliderect(us2):
                for i in range(len(bbdrawing)):
                    bbdrawing[i] = True
                for i in range(len(drawing3)):
                    drawing3[i] = True
                guy[angle] = 0
                guy[X] = 250
                guy[Y] = 478
                guy[score] = 0
                guy[progress] = 0
                guy[power] = False
                guy[shotY] = guy[Y]
                die.play(0)
                time.wait(300)

def checkPowerup(guy):
    hitbox = Rect(guy[X],guy[Y],29,31)
    if hitbox.colliderect(powerup):
        guy[power] = True

def checkProgress(guy,progress):
    if guy[page] == "lvl1":
        if guy[progress] < 135:
            guy[progress] += 3/60
    if guy[page] == "lvl2":
        if guy[progress] < 135:
            guy[progress] += 3/60
    if guy[page] == "lvl3":
        if guy[progress] <125:
            guy[progress] += 3/60

def levelEnd(guy):
    if guy[page] == "lvl1":
        if guy[X] > 14500:
            guy[finalscore] = guy[score]
            screen.blit(lvlcom,(50,300))
            back = draw.rect(screen,darkblue,(350,400,120,50))
            screen.blit(backbutton,(350,400))
            if back.collidepoint(mx,my):
                draw.rect(screen,(0,0,0),(350,400,120,50),1)
            if mb[0] == 1 and back.collidepoint(mx,my):
                guy[page] = "menu"
                guy[X] = 250
                guy[Y] = 478
                guy[score] = 0
                guy[progress] = 0
                guy[power] = False
                for i in range(len(drawing)):
                    drawing[i] = True
                    
    if guy[page] == "lvl2":
        if guy[X] > 15400:
            guy[finalscore] = guy[score]
            screen.blit(lvlcom,(50,300))
            back = draw.rect(screen,darkblue,(350,400,120,50))
            screen.blit(backbutton,(350,400))
            if back.collidepoint(mx,my):
                draw.rect(screen,(0,0,0),(350,400,120,50),1)
            if mb[0] == 1 and back.collidepoint(mx,my):
                guy[page] = "menu"
                guy[X] = 250
                guy[Y] = 478
                guy[score] = 0
                guy[progress] = 0
                guy[power] = False
                for i in range(len(drawing2)):
                    drawing2[i] = True
                    
    if guy[page] == "lvl3":
        if bosslist[bossbeat] == True:
            guy[finalscore] = guy[score]
            screen.blit(lvlcom,(50,300))
            back = draw.rect(screen,darkblue,(350,400,120,50))
            screen.blit(backbutton,(350,400))
            if back.collidepoint(mx,my):
                draw.rect(screen,(0,0,0),(350,400,120,50),1)
            if mb[0] == 1 and back.collidepoint(mx,my):
                guy[page] = "menu"
                bosslist[bossHP] = 30
                bosslist[bossbeat] = False
                guy[X] = 250
                guy[Y] = 478
                guy[score] = 0
                guy[progress] = 0
                guy[power] = False
                guy[shotX] = 0
                guy[shotY] = guy[Y]
                for i in range(len(drawing3)):
                    drawing3[i] = True
                for i in range(len(bbdrawing)):
                    bbdrawing[i] = True
                
def checkPowerup(guy):
    hitbox = Rect(guy[X],guy[Y],30,30)
    if hitbox.colliderect(powerup):
        guy[power] = True

def goldText(guy):
    if guy[page] == "store":
        font.init()
        timesFont = font.SysFont("Times New Roman", 20)
        txt = timesFont.render("YOUR GOLD: %s" % guy[finalscore], True, (0,0,255))
        screen.blit(txt,(100,530))
        font.quit()
        del timesFont
        
def SpinJump(guy):
    if guy[page] == "lvl1":
        jump(guy)
        if guy[jumping] == True:
            guy[angle] -= 7 #if guy jumping make guy spin
            if guy[angle] < -360: 
                guy[angle] = 0 #reset after 1 full rotation so it doesnt go below -360
        if guy[jumping] == False and guy[VY] > 1:
            guy[angle] -= 7 #if guy is falling make guy spin
            if guy[angle] < -360: 
                guy[angle] = 0 #so angle resets after 1 full rotation
        elif guy[jumping] == False:
            #makes angle based on what angle it lands
            #1st area
            if guy[angle] >= -315 and guy[angle] <=-224:
                guy[angle] = -270
            #2nd area
            if guy[angle] >= -225 and guy[angle] <=-134:
                guy[angle] = -180
            #3rd area
            if guy[angle] >= -135 and guy[angle] <=-44:
                guy[angle] = -90
            #4th area
            if guy[angle] <= -314 and guy[angle] >= -360:
                guy[angle] = 0
            if guy[angle] <= 0 and guy[angle] >= -45:
                guy[angle] = 0
                
    if guy[page] == "lvl2":
        jump(guy)
        if guy[jumping] == True:
            guy[angle] -= 7 
            if guy[angle] < -360: 
                guy[angle] = 0 
        if guy[jumping] == False and guy[VY] > 1:
            guy[angle] -= 7 
            if guy[angle] < -360: 
                guy[angle] = 0 
        elif guy[jumping] == False:
            #makes angle based on what angle it lands
            #1st area
            if guy[angle] >= -315 and guy[angle] <=-224:
                guy[angle] = -270
            #2nd area
            if guy[angle] >= -225 and guy[angle] <=-134:
                guy[angle] = -180
            #3rd area
            if guy[angle] >= -135 and guy[angle] <=-44:
                guy[angle] = -90
            #4th area
            if guy[angle] <= -314 and guy[angle] >= -360:
                guy[angle] = 0
            if guy[angle] <= 0 and guy[angle] >= -45:
                guy[angle] = 0
                
    if guy[page] == "lvl3":
        if guy[X] <= 8000 or guy[X] >= 12500: #if guy is rightside up
            jump(guy)
            if guy[angle] > 0:
                guy[angle] == 0
            if guy[jumping] == True:
                guy[angle] -= 7 
                if guy[angle] < -360: 
                    guy[angle] = 0 
            if guy[jumping] == False and guy[VY] > 1:
                guy[angle] -= 7 
                if guy[angle] < -360: 
                    guy[angle] = 0 
            elif guy[jumping] == False:
                #makes angle based on what angle it lands
                #1st area
                if guy[angle] >= -315 and guy[angle] <=-224:
                    guy[angle] = -270
                #2nd area
                if guy[angle] >= -225 and guy[angle] <=-134:
                    guy[angle] = -180
                #3rd area
                if guy[angle] >= -135 and guy[angle] <=-45:
                    guy[angle] = -90
                #4th area
                if guy[angle] <= -314 and guy[angle] >= -360:
                    guy[angle] = 0
                if guy[angle] <= 0 and guy[angle] >= -45:
                    guy[angle] = 0
        else: #if guy is upside down
            upsidedownjump(guy)
            if guy[angle] > 0:
                guy[angle] == 0
            if guy[jumping] == True:
                guy[angle] -= 7 
                if guy[angle] < -360: 
                    guy[angle] = 0 
            if guy[jumping] == False and guy[VY] > 1:
                guy[angle] -= 7 
                if guy[angle] < -360: 
                    guy[angle] = 0 
            elif guy[jumping] == False:
                #makes angle based on what angle it lands
                #1st area
                if guy[angle] >= -315 and guy[angle] <=-224:
                    guy[angle] = -270
                #2nd area
                if guy[angle] >= -225 and guy[angle] <=-134:
                    guy[angle] = -180
                #3rd area
                if guy[angle] >= -135 and guy[angle] <=-45:
                    guy[angle] = -90
                #4th area
                if guy[angle] <= -314 and guy[angle] >= -360:
                    guy[angle] = 0
                if guy[angle] <= 0 and guy[angle] >= -45:
                    guy[angle] = 0
running = True
clock = time.Clock()

storelist = [25,50]
guy = [250,478,0,False,0,0,"menu",0,"None",250,0,False,0]
bosslist = [30,True,9,600,False]

platforms = (255,0,0,255) #platform mask
walls = (0,0,255,255) #wall mask

powerup = Rect(686,360,20,20)

#finds x and y from text files
jumpblocks = []
for i in range(0,len(jblockpos),2):
    jumpblocks.append(Rect(int(jblockpos[i]),int(jblockpos[i+1]),30,30))
breakblocks = []
for i in range(0,len(bblockpos),2):
    breakblocks.append(Rect(int(bblockpos[i]),258,20,250))
upsidespikes = []
for i in range(0,len(upsidepos),2):
    upsidespikes.append(Rect(int(upsidepos[i]),int(upsidepos[i+1]),20,20))
upsidespikes2 = []
for i in range(0,len(upsidepos2),2):
    upsidespikes2.append(Rect(int(upsidepos2[i]),int(upsidepos2[i+1]),20,20))
spikes = []
for i in range(0,len(spikepos),2):
    spikes.append(Rect(int(spikepos[i]),int(spikepos[i+1]),20,20))
spikes2 = [Rect(2000,478,20,30)]
for i in range(0,len(spikepos2),2):
    spikes2.append(Rect(int(spikepos2[i]),int(spikepos2[i+1]),20,30))
spikes3 = [Rect(2000,478,20,30)]
for i in range(0,len(spikepos3),2):
    spikes3.append(Rect(int(spikepos3[i]),int(spikepos3[i+1]),20,30))
coins = [Rect(600,490,10,10)]
for i in range(0,len(coinposlvl1),2):
    coins.append(Rect(int(coinposlvl1[i]),int(coinposlvl1[i+1]),10,10))
coins2 = []
for i in range(0,len(coinposlvl2),2):
    coins2.append(Rect(int(coinposlvl2[i]),int(coinposlvl2[i+1]),10,10))
coins3 = []
for i in range(0,len(coinposlvl3),2):
    coins3.append(Rect(int(coinposlvl3[i]),int(coinposlvl3[i+1]),10,10))
    
drawing = []
for i in range(len(coins)):
    drawing.append(True)
drawing2 = []
for i in range(len(coins2)):
    drawing2.append(True)
drawing3 = []
for i in range(len(coins3)):
    drawing3.append(True)
bbdrawing = []
for i in range(len(breakblocks)):
    bbdrawing.append(True)

while running:
    click = False
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            click = True
    #playing songs
    #------------------------------
            
    #so music doesnt stop in the ingamemenu
    if guy[page] == "lvl1" or guy[page] == "ingamemenu" or guy[page] == "instructions2":
        if guy[X] == 257:
            song1.play(1)
        if guy[X] == 250:
            song1.stop()
    elif guy[page] != "lvl1":
        song1.stop()
        
    if guy[page] == "lvl2" or guy[page] == "ingamemenu" or guy[page] == "instructions2":
        if guy[X] == 257:
            song2.play(1)
        if guy[X] == 250:
            song2.stop()
    elif guy[page] != "lvl2":
        song2.stop()
        
    if guy[page] == "lvl3" or guy[page] == "ingamemenu" or guy[page] == "instructions2":
        if guy[X] == 256:
            song3.play(1)
        if guy[X] == 250:
            song3.stop()
    elif guy[page] != "lvl3":
        song3.stop()
    #------------------------------
        
    mx,my = mouse.get_pos()
    mb = mouse.get_pressed()

    if guy[page] == "lvl1" or guy[page] == "lvl2" or guy[page] == "lvl3":

        move(guy)
        checkSpikes(guy,spikes,spikes2,spikes3)
        checkPlatforms(guy,platforms)
        checkWalls(guy,walls)
        drawScene(screen, guy,drawing)
        checkProgress(guy,progress)
        checkPowerup(guy)
        levelEnd(guy)
        SpinJump(guy)
        
    menu(guy,screen,page)
    goldText(guy)

    clock.tick(60)
    display.flip()
quit()
