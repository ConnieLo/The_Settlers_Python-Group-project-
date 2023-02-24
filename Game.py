import pygame
import button
import crosshair
import dice
import player
import draw_board
from draw_board import co_ords, drawNumbers
import random

# Initialize Pygame
pygame.init()
# Set screen size and title
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catan")
# load the icon for the game
icon = pygame.image.load('resources/icon.png').convert_alpha()
# add the icon
pygame.display.set_icon(icon)
###################### Universal instances ##################################################

# crosshair
pygame.mouse.set_visible(False)
# load crosshair image & create a crosshair object and add it to a sprite group
crosshair = crosshair.crosshair("resources/cursor_fist.gif", "resources/cursor.gif")
crosshair_group = pygame.sprite.Group(crosshair)
crosshair_group.add(crosshair)

# load button images
start_img = pygame.image.load('resources/Play.png').convert_alpha()
quit_img = pygame.image.load('resources/Quit.png').convert_alpha()
start_img2 = pygame.image.load('resources/Play2.png').convert_alpha()
quit_img2 = pygame.image.load('resources/Quit2.png').convert_alpha()

#################### Main menu Stage #####################################################
# load the background image for the main menu
background = pygame.image.load('resources/landscape.jpg').convert_alpha()
# Scale the background image to fit the screen size
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# create button instance
start_button = button.Button(SCREEN_WIDTH/5, SCREEN_HEIGHT/2.5, start_img, start_img2)
quit_button = button.Button(SCREEN_WIDTH/1.8, SCREEN_HEIGHT/2.5, quit_img, quit_img2)
#################### Main menu Stage END#######################################################


#################### Game Stage ###############################################################
quit_button2 = button.Button(SCREEN_WIDTH*0, SCREEN_HEIGHT*0, quit_img, quit_img2)

# dice instance
dice = dice.Dice(1078, 539, 50)# define dice

# Player instance
# RBG value
BLACK = (0, 0, 0)
# Set the font size
font_size = 30
# Load the Pygame Serif font
font = pygame.font.Font(None, font_size)
# create a player instance
player1 = player.player("Player", BLACK)

# random number generator
numbers = [random.randint(1, 12) for _ in range(len(co_ords))]

# font1 # I did it this way due to the performance, so it does not load up the font all the time
font1 = pygame.font.SysFont(None, 36, bold=True) # setting up the font to be bold
######################## Game Stage END #######################################################

#################### Game Stage Function ######################################################
def game():
    clock = pygame.time.Clock()
    running = True
    diceRolling = False #boolean for event loop
    dRollCount = 0
    while running:
        screen.fill((79, 129, 189))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            ####################################################################################
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                if (dice.d1X <= mouseX <= dice.d2X+dice.dimens) and (dice.d1Y <= mouseY <= dice.d1Y+dice.dimens):
                    if diceRolling == False:
                        pygame.time.set_timer(dice.EVENT, 100)
                        diceRolling = True #so you can't retrigger dice roll when its already rolling
                        dRollCount = 0 #counting for animation of dice roll

            elif event.type == dice.EVENT:
                if dRollCount == 10: #num of seconds for animation x10
                    dRoll = dice.roll(screen) #gets value of roll
                    value = dRoll[0] + dRoll[1] # adds up both of the dice values
                    pygame.time.set_timer(dice.EVENT, 0)
                    diceRolling = False
                    print(value) # prints out the values of the two dice
                else:
                    dice.roll(screen) #temp display of dice while rolling
                    dRollCount += 1

        
        #display static dice when not rolling
        dice.display(screen)


        # board
        draw_board.main(screen)

        # Draw random numbers in the center of each hexagon
        drawNumbers(screen, numbers, font1)

        # quit button
        if quit_button2.draw(screen):
            print('QUIT')
            running = False

        # Display the player's name and score
        player1.display(screen, font, 10, SCREEN_HEIGHT-100)


        # crosshair
        crosshair_group.draw(screen)
        crosshair_group.update()
        #########################################################################
        clock.tick(60)
        pygame.display.flip()
############################# Main Game Loop #################################################
# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ####################################################################
    # buttons
    screen.blit(background, (0, 0))
    if start_button.draw(screen):
        print('START')
        game()
    if quit_button.draw(screen):
        print('QUIT')
        running = False

    # crosshair
    crosshair_group.draw(screen)
    crosshair_group.update()
    crosshair.switch_image([start_button, quit_button])
    #########################################################################
    pygame.display.update()
# Quit Pygame
pygame.quit()

