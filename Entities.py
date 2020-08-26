#-------------------------------------------------------------------------------
# Name:        Entities
#-------------------------------------------------------------------------------
#import needed modules
import pygame
from Player import play
from Resources import Constants as con
from Resources import Sprite_lists as spr
from Resources import Images as img
#parent class for every object that is on the screen except background and player.
#pass in image and position arguements when instantiated.
class Sprite(pygame.sprite.Sprite):
    """Sprite class to make objects on screen excluding background and player.
    """
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.initial_x = x
        self.initial_y = y
        self.initial_counter = 0
        self.to_add = []
        self.reset()
    #reset every sprite to its original x and y values. added a counter for
    #traps to be defused if you reset level, otherwise traps stay activated
    def reset(self):
        self.rect.x = self.initial_x
        self.rect.y = self.initial_y
        self.counter = self.initial_counter


#child class for non-moving hazards, like spikes.
class Hazard(Sprite):
    def update(self):
        #check collision between two rects only instead of one rect and a group
        hit = pygame.sprite.collide_rect(self, play)
        if hit:
            #We found sprite.kill() by exploring what pygame how to offer,
            #it is terrible as it only makes the sprite invisible but still
            #leave's around the sprite's hitbox, which would be troublesome for
            #alot of things, for example the death counter will keep on adding
            #for the time a AutoHazard is inside a player's rect.
            #a fix for this is to set player's position to something else,
            #hence the play.dead() function.
            play.kill()
            play.dead()
#child class for all traps.
class AutoHazard(Sprite):
    #kind is a optional arguement, if nothing is passed for kind, then it is
    #automatically set to 'default'
    def set(self, x_speed, y_speed, kind = 'default'):
        self.kind = kind
        #set the trap again if its counter is reset
        if self.counter == 0:
            self.trigger()
        #what makes the trap move
        if self.counter == 1:
            self.rect.x += x_speed
            self.rect.y += y_speed
        #super secret developer code to test if levels worked, you can use it yourself
        #if level is too hard, just jump right after player respawns
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t] and keys[pygame.K_f]:
            self.counter = 1
        else:
            self.trigger()
        #con.height_kill and con.width_kill kills the trap if traps goes too far
        #this code is crucial as unkilled sprites going off screen forever will make
        #"ghost sprites", which after passing certain x or y value's will reappear on
        #the screen with no hitbox
        if self.rect.x < -100 or self.rect.x > con.width_kill or self.rect.y < -100 or self.rect.y > con.height_kill:
            self.kill()
            #a list used to respawn all traps if reset_level is passed.
            con.killed_sprites.append(self)
        #if hit, kill player
        hit = pygame.sprite.collide_rect(self, play)
        if hit:
            play.dead()
    #makes rect for trap if needed
    def make_rect(self, x, y, width, length):
        self.trap_rect = Trap_rect(x, y, width, length)
    #function to determine if traps will be triggered
    #default makes is used for normal traps that shoot up or down,
    #special is used to for traps that will activate only if player is within
    #special x and y positions, like the horizontal trap in level 1
    def trigger(self):
        if self.kind == 'default':
            if play.rect.x >= self.rect.x - 83:
                self.counter = 1
        if self.kind == 'special':
            if pygame.sprite.collide_rect(self.trap_rect, play):
                self.counter = 1

#a hitbox rect used to activate specific traps with specific parameters
class Trap_rect(pygame.sprite.Sprite):
    def __init__(self, x, y, width, length):
        super().__init__()
        self.image = pygame.Surface([width,length])
        #added this to put rects at right places more accurately
        #changes transparency of rect, 0 is invisible and 200 is no transparency
        self.image.set_alpha(0)


        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        spr.all_sprites.add(self)
        con.leftover_rects.append(self)
    #as this is a parent class, a reset function is needed with no statements
    #otherwise program will crash
    def reset(self):
        pass

