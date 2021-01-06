#-------------------------------------------------------------------------------
# Name:        T.V. Man's Adventure

# Author:      Keven Qiu
#-------------------------------------------------------------------------------
#imports all modules
import pygame, sys
from Player import play
from Maps import *
from Resources import Constants as con
from Resources import Sprite_lists as spr
from Resources import Images as img
pygame.init()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#a function for ending program
def endProgram():
    pygame.quit()
    sys.exit()

#set all screen constants
menu_size = (750, 670)
screen = pygame.display.set_mode(con.menu_size)
font = pygame.font.SysFont(None, 48)
pygame.display.set_caption("T.V. Man")
pygame.display.set_icon(img.back_img)

#main menu function
def menu():
    timer = 0
    bkcolor = con.BRED
    pygame.mouse.set_visible(True)
    pygame.display.set_mode(con.menu_size)

    while True:
        screen.fill(bkcolor)

        gameSelector = []
        gameSelector.append(pygame.Rect(180, 450, 400, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endProgram()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    endProgram()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if gameSelector[0].collidepoint(pygame.mouse.get_pos()):
                    mainGame()
                    break

        for rect in gameSelector:
            pygame.draw.rect(screen, con.RED, rect)

        drawtext("T.V Man's Journey", screen, 40, 230, pygame.font.SysFont(None, 112), con.BLUE)
        drawtext("By: Keven Qiu", screen, 150, 330, pygame.font.SysFont("Comic Sans MS", 20), con.BLUE)
        drawtext("Click here to start game", screen, 190, 485, font, con.BLACK)
        drawtext("If you dare...", screen, 190, 600, pygame.font.SysFont(None, 16), con.GREEN)
        clock.tick(60)
        timer += 1
        if timer % 100 == 0:
            bkcolor = con.BRED
        elif timer % 50 == 0:
            bkcolor = con.LIGHTGREEN
        pygame.display.update()

#function to draw text
def drawtext(text, surface, x, y, font = font, color = con.WHITE):
    textObj = font.render(text, 1, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)
    screen.blit(textObj, textRect)

def endGame():
    #set conditions if you complete the level for the screen
    pygame.mouse.set_visible(True)
    pygame.display.set_mode(con.menu_size)
    screen.fill(con.BRED)
    drawtext("Whoop de doo!", screen, 200, 325, font, con.BLUE)
    drawtext("Ya only died " + str(play.death_counter) + " times hehe", screen, 160, 360, font, con.GREEN)
    clock.tick(60)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endProgram()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                endProgram()

def mainGame():
    #start_ticks = pygame.time.get_ticks()
    #display = pygame.Surface([2000,600])
    pygame.display.set_caption("T.V Man")
    pygame.mouse.set_visible(False)
    pygame.display.set_mode((con.width, con.height))

    #instructions for the game
    def intro():
            drawtext('Traverse through each level and avoid every trap!', screen, 0,0)
            drawtext('Arrow keys to move and jump. Press R to respawn!', screen, 0,32)

    #death counter added for fun
    def death_counter():
        drawtext('Deaths: ' + str(play.death_counter), screen, 1300, 0)
    #configure level switching

    #append all levels to one list
    #set level 1
    level_list = []
    level_list.append(Level_01)
    level_list.append(Level_02)
    level_list.append(Level_03)
    current_level = level_list[con.level_no]()



    #main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endProgram()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    play.go_left()
                elif event.key == pygame.K_RIGHT:
                    play.go_right()
                elif event.key == pygame.K_UP:
                    #jump
                    play.yahoo()
                elif event.key == pygame.K_r:
                    #function for resetting every sprite's position back to where they were initially.
                    reset_level()
                elif event.key == pygame.K_ESCAPE:
                    endProgram()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and play.change_x < 0:
                    play.stop()
                if event.key == pygame.K_RIGHT and play.change_x > 0:
                    play.stop()

        screen.blit(img.back_img, [-300,-100])
        spr.all_sprites.draw(screen)
        spr.all_sprites.update()
        #game instructions
        intro()
        death_counter()
        #set level 1 traps
        current_level.set_level()
        #initiate next level, clean previous level's tiles and rects left behind
        if play.rect.x >= con.width -50:
            con.level_no += 1
            #new code, remove all elements in a list
            del con.killed_sprites[:]
            play.reset()
            spr.clean_groups()
            spr.all_sprites.remove(con.leftover_rects)
            try:
                current_level = level_list[con.level_no]()
            except:
                endGame()
            current_level.set_level()
        #con.screen.blit(pygame.transform.scale(display, con.window_size),(0,0))
        pygame.display.update()
        clock.tick(60)

#start game menu
menu()
