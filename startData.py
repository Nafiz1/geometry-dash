from pygame import *

init()
col = (255,0,255,255)


pic = image.load("GeoBackgroundlevel3withdots.png")
out = open("coinslvl3coords.txt","w")
for x in range(pic.get_width()):
    for y in range(pic.get_height()):
        c = tuple(pic.get_at((x,y)))
        if col == c:
            out.write("%d,%d\n" % (x,y))
out.close()
    

