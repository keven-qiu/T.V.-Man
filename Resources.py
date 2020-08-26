#-------------------------------------------------------------------------------
# Name:        Resources
#-------------------------------------------------------------------------------
import pygame

pygame.init()
#to load images in separate files, you need to set
#below statement first
pygame.display.set_mode([0,0])

#images class
#.convert_alpha() removes lag caused by images being drawn on screen
class Images():
    enemy1 = pygame.image.load("enemy3.png").convert_alpha()
    enemy2 = pygame.image.load("enemy2.png").convert_alpha()
    enemy3 = pygame.image.load("enemy1.png").convert_alpha()
    grass_img = pygame.image.load("grass.png").convert_alpha()
    dirt_img = pygame.image.load("dirt.png").convert_alpha()
    spike_img = pygame.image.load("spike.png").convert_alpha()
    lul_img = pygame.image.load("lul.png").convert_alpha()
    back_img = pygame.image.load("back.png").convert_alpha()
    zulul_img = pygame.image.load("zulul.png").convert_alpha()

#all constants
class Constants():
    #COLOURS
    AMERICANRED=(178,34,52)
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)
    BLUE     = (   0,   0, 255)
    LIGHTGREEN = (125, 125, 255)
    BRED     = ( 203,  65,  84)
    #Variables
    width_kill = 1600
    height_kill = 700
    menu_size = (750, 670)
    width = 1500
    height = 600
    level_no = 0
    killed_sprites = []
    leftover_rects = []
    ToClean = []
    clean_onscreenspr = []
#class storing all groups and
class Sprite_lists():
    all_sprites = pygame.sprite.Group()
    objects_sprites = pygame.sprite.Group()
    hazard_sprites = pygame.sprite.Group()
    projectile_sprites = pygame.sprite.Group()
    hostile_sprites = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    #iterates through every parent class that inherit from
    #pygame.sprite.Sprite class in pygame and calls in reset
    #function for each of them
    def reset_sprites():
        for sprites in Sprite_lists.all_sprites:
            sprites.reset()
        Sprite_lists.all_sprites.remove(Constants.clean_onscreenspr)
    def clean_groups():
        Sprite_lists.objects_sprites.empty()
        Sprite_lists.all_sprites.remove(Constants.ToClean)
