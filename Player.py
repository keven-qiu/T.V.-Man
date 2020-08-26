#-------------------------------------------------------------------------------
# Name:        Player
#-------------------------------------------------------------------------------
import pygame
from Resources import Images as img
from Resources import Constants as con
from Resources import Sprite_lists as spr
#make player class
class Guy(pygame.sprite.Sprite):
    """Create player class. Collision, jumping, movement, and gravity
    for player is written here.
    """
    def __init__(self):
        super().__init__()
        self.image = img.enemy3
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 60
        self.change_x = 0
        self.change_y = 0

        self.death_counter = 0

    def yahoo(self):
        #statements to check if it is okay to jump
        self.rect.y += 2
        collide = pygame.sprite.spritecollide(self, spr.objects_sprites, False)
        self.rect.y -= 2

        if len(collide) > 0 or self.rect.bottom >= con.height:
            self.change_y = -16

    #movement
    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0

    def dead(self):
        #method that is called
        self.kill()
        self.rect.x = 1
        self.rect.y = 1

        self.death_counter += 1



    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .50

        if self.rect.y >= con.height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = con.height - self.rect.height

    def reset(self):
        self.rect.x = 0
        self.rect.y = 60


    def update(self):
        #calculate gravity, put it in main program loop
        self.calc_grav()
        #update movement every frame
        self.rect.x += self.change_x
        #collision code. Builtin pygame functions to check if
        #collision between one sprite and sprite group is true or not.
        collision = pygame.sprite.spritecollide(self, spr.objects_sprites, False)
        for collide in collision:
            #builtin rect functions. if collision from right, then equal left side
            #of object, vice versa.
            if self.change_x > 0:
                self.rect.right = collide.rect.left
            else:
                self.rect.left = collide.rect.right
        #updated every frame
        self.rect.y += self.change_y
        #call in collision to check if collision happens when you jump on platforms
        #or bounce of them
        collision = pygame.sprite.spritecollide(self, spr.objects_sprites, False)
        for collide in collision:
            if self.change_y > 0:
                self.rect.bottom = collide.rect.top
            if self.change_y < 0:
                self.rect.top = collide.rect.bottom
            #if bounce, then instead of "sticking" on a platforms bottom side,
            #you go straight down.
            self.change_y = 0
#instantiate player class to be used in Maps, Entities, and main files.
play = Guy()
spr.all_sprites.add(play)
