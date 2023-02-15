import pygame
import dice

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (width, height).
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))


# Set title of the window
pygame.display.set_caption("Catan Game")

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 153, 213)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen.fill(BLUE)

# Loop until the user clicks the close button.
done = False

pygame.display.update()

#define dice
dice = dice.Dice()
diceRolling = False #boolean for event loop

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONUP:
            mouseX, mouseY = pygame.mouse.get_pos()
            if (dice.d1X <= mouseX <= dice.d2X+dice.dimens) and (dice.d1Y <= mouseY <= dice.d1Y+dice.dimens):
                if diceRolling == False:
                    pygame.time.set_timer(dice.EVENT, 100)
                    diceRolling = True #so you can't retrigger dice roll when its already rolling
                    dRollCount = 0 #counting for animation of dice roll

        elif event.type == dice.EVENT:
            if dRollCount == 10: #num of seconds for animation x10
                dRoll = dice.roll() #gets value of roll
                pygame.time.set_timer(dice.EVENT, 0)
                diceRolling = False
                
            else:
                dice.display(dice.num()) #temp display of dice while rolling
                dRollCount += 1

    #display static dice when not rolling
    if diceRolling == False:
        dice.display()


    # Limit to 60 frames per second
    clock.tick(60)

    # Update the screen with what we've drawn.
    pygame.display.flip()

# Close the window and quit.
pygame.quit()