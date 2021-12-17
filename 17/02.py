minx = 150
maxx = 193
miny = -136
maxy = -86

c = 0
for x in range(maxx + 1):
    for y in range(miny, -miny):
        posx, posy = 0, 0
        velx, vely = x, y
        while posx <= maxx and posy >= miny:
            posx += velx
            posy += vely
            if velx:
                velx -= 1
            vely -= 1
            if minx <= posx <= maxx and miny <= posy <= maxy:
                c += 1
                break

print(c)