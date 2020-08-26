#-------------------------------------------------------------------------------
# Name:        Maps
#-------------------------------------------------------------------------------
import pygame
from Player import play
from Resources import Sprite_lists as spr
from Resources import Constants as con
from Resources import Images as img
from Entities import Sprite
from Entities import AutoHazard
from Entities import Hazard
#load text file by passing it through this function
#iterates through every line and appends it to maps
def load_map(path):
    maps = []
    f = open(path, "r")
    for line in f:
        tempmaps = line.split(",")
        tempmaps[-1] = tempmaps[-1].strip("\n")
        tempmaps = [int(i) for i in tempmaps]
        maps.append(tempmaps)
    f.close()
    return maps
#load maps
rage_map = load_map("rage_map.txt")
de_dirt = load_map("de_dirt.txt")
de_mirage = load_map("de_mirage.txt")

class Create_level(object):
    """Parent class to create a level by passing loaded maps
    from text files through the load_map function and adding tiles for every
    number in txt file
    """
    def load_map(self, level_map):
        #create a wall for every level where the player spawns,
        #so that player cannot go back
        wall = Sprite(pygame.Surface([1,700]), -1,0)
        spr.objects_sprites.add(wall)
        spr.all_sprites.add(wall)
        current_map = list(level_map)
        y = 0
        #iterate through every layer within a
        #list and make tiles based on where the numbers are.
        #if function finds tile == 0, then make dirt sprite,
        #if 1, make grass sprite, else if not 0 or 1, make nothing
        #every three in txt file represents an empty space
        for layer in current_map:
            x = 0
            for tile in layer:
                if tile == 0:
                    Terr = Sprite(img.dirt_img, x*32, y*16)
                    spr.objects_sprites.add(Terr)
                    spr.all_sprites.add(Terr)
                    con.ToClean.append(Terr)
                if tile == 1:
                    Terr = Sprite(img.grass_img, x*32, y*16)
                    spr.objects_sprites.add(Terr)
                    spr.all_sprites.add(Terr)
                    con.ToClean.append(Terr)
                x += 1
            y += 1

class Level_01(Create_level):
    def __init__(self):
        """Child class inheriting from Create_level. Loads a map for a level and place
        traps where we want them to be
        """
        self.load_map(rage_map)

        self.trap = AutoHazard(img.lul_img, 1000, con.height - 50)
        spr.all_sprites.add(self.trap)

        self.trap_list = []
        var = 50
        while var < 200:
            self.cluster_traps = AutoHazard(img.zulul_img, 480 + var, -95)
            self.cluster_traps.make_rect(480, 435, 200, 100)
            spr.all_sprites.add(self.cluster_traps)
            self.trap_list.append(self.cluster_traps)
            var += 50

        self.trap3 = AutoHazard(img.lul_img, 700, con.height - 50)
        self.trap3.make_rect(936, 536, 600,500)
        spr.all_sprites.add(self.trap3)

        #make special trap with certain parameters
        #if player collides with the rect then trap triggers
        self.trap4 = AutoHazard(img.lul_img, 1500, 240)
        self.trap4.make_rect(596, 260, 156, 34)
        spr.all_sprites.add(self.trap4)

        self.trap5 = AutoHazard(img.zulul_img, 1230, -50)
        spr.all_sprites.add(self.trap5)

        self.trap2 = AutoHazard(img.lul_img, 800, con.height - 50)
        spr.all_sprites.add(self.trap2)

    def set_level(self):
        #set every trap's speed and type
        self.trap3.set(20, 0, 'special')

        for traps in self.trap_list:
            traps.set(0, 27, 'special')

        self.trap4.set(-25, 0, 'special')

        self.trap5.set(0, 37)

        self.trap2.set(0, -20)

        self.trap.set(0, -20)

#same as Level_01
class Level_02(Create_level):
    def __init__(self):
        self.load_map(de_dirt)

        self.trap_list = []
        var = 50
        while var < 350:
            self.cluster_traps = AutoHazard(img.zulul_img, -65, 60 + var)
            self.cluster_traps.make_rect(250, 63, 25, 300)
            self.trap_list.append(self.cluster_traps)
            spr.all_sprites.add(self.cluster_traps)
            var += 50

        if play.rect.x >= con.width -50:
            spr.all_sprites.remove(self.cluster_traps, self.trap_list)

        self.trap = AutoHazard(img.lul_img, 1230, 176)
        self.trap.make_rect(342, 264, 100, 25)
        spr.all_sprites.add(self.trap)

        self.trap2 = AutoHazard(img.zulul_img, 699, -65)
        self.trap2.make_rect(672, 464, 86, 72)
        spr.all_sprites.add(self.trap2)

        self.trap3 = AutoHazard(img.lul_img, 699, -65)
        spr.all_sprites.add(self.trap3)

        self.trap4 = AutoHazard(img.zulul_img, con.width + 50, 336)
        self.trap4.make_rect(1216, 336, 156, 50)
        spr.all_sprites.add(self.trap4)

    def set_level(self):
        for traps in self.trap_list:
            traps.set(3, 0, 'special')

        self.trap4.set(-7, 0, 'special')

        if play.rect.x >= con.width -50:
            spr.all_sprites.remove(self.cluster_traps, self.trap_list)
            spr.all_sprites.remove(self.trap4)

        self.trap.set(-20, 0, 'special')

        self.trap3.set(0,30)

        self.trap2.set(0, 2, 'special')

class Level_03(Create_level):
    def __init__(self):
        """Child class inheriting from Create_level. Loads a map for a level and place
        traps where we want them to be
        """
        self.load_map(de_mirage)

        self.trap = AutoHazard(img.lul_img, 1000, con.height - 50)
        spr.all_sprites.add(self.trap)

        self.trap3 = AutoHazard(img.lul_img, 700, con.height - 50)
        self.trap3.make_rect(1100,250,150,150)
        spr.all_sprites.add(self.trap3)

        #make special trap with certain parameters
        #if player collides with the rect then trap triggers
        self.trap4 = AutoHazard(img.lul_img, 1500, 240)
        self.trap4.make_rect(596, 260, 156, 34)
        spr.all_sprites.add(self.trap4)

        self.trap5 = AutoHazard(img.zulul_img, 1230, -50)
        spr.all_sprites.add(self.trap5)

        self.trap2 = AutoHazard(img.lul_img, 800, con.height - 50)
        spr.all_sprites.add(self.trap2)

        self.spike1 = Hazard(img.spike_img, 970, con.height - 100)
        spr.all_sprites.add(self.spike1)

        self.spike2 = Hazard(img.spike_img, 1220, con.height - 30)
        spr.all_sprites.add(self.spike2)

    def set_level(self):
        #set every trap's speed and type
        self.trap3.set(14, -15, 'special')

        self.trap4.set(-25, 0, 'special')

        self.trap5.set(0, 37)

        self.trap2.set(0, -20)

        self.trap.set(0, -20)
#this is how a level is reset if you die
#spawn the player back in, add in traps that were killed by going off screen.
def reset_level():
        spr.all_sprites.add(play)
        spr.all_sprites.add(con.killed_sprites)
        #command to delete all elements in killed_sprites, otherwise it keeps on adding infinitely
        del con.killed_sprites[:]
        #weird bug where if you keep spamming the R button, you descend down faster and faster,
        #so make player.change_y to 0 to avoid this
        play.change_y = 0
        #call in reset function from Resources
        spr.reset_sprites()
