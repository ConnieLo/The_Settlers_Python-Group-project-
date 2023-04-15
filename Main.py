import pygame

from classes.button import Button
from classes import ui, dice
from classes.game_master import GameMaster, draw



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
crosshair = ui.crosshair("resources/cursor_fist.gif", "resources/cursor.gif")
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
start_button = Button(SCREEN_WIDTH / 5, SCREEN_HEIGHT / 2.5, start_img, start_img2)
quit_button = Button(SCREEN_WIDTH / 1.8, SCREEN_HEIGHT / 2.5, quit_img, quit_img2)
#################### Main menu Stage END#######################################################


#################### Game Stage ###############################################################
quit_button2 = Button(SCREEN_WIDTH * 0, SCREEN_HEIGHT * 0, quit_img, quit_img2)

# dice instance
dice = dice.Dice(1120, 670, 50)  # define dice

# Load card images
Clay = pygame.image.load('resources/cards/brick.jpg').convert_alpha()
Sheep = pygame.image.load('resources/cards/wool.jpg').convert_alpha()
Ore = pygame.image.load('resources/cards/ore.jpg').convert_alpha()
Wood = pygame.image.load('resources/cards/lumber.jpg').convert_alpha()
Wheat = pygame.image.load('resources/cards/wheat.jpg').convert_alpha()

# aj work loading images
cards_cards = pygame.image.load('resources/cards/cards_cards.jpg').convert_alpha()
cities_cards = pygame.image.load('resources/cards/cities_cards.jpg').convert_alpha()
development_cards = pygame.image.load('resources/cards/development_cards.jpg').convert_alpha()
resource_cards = pygame.image.load('resources/cards/resource_cards.jpg').convert_alpha()
road_cards = pygame.image.load('resources/cards/road_cards.jpg').convert_alpha()
settlement = pygame.image.load('resources/cards/settlement.jpg').convert_alpha()
victory_points = pygame.image.load('resources/cards/victory_points.jpg').convert_alpha()


# loading army and road
largest_army = pygame.image.load('resources/Top/largest_army.jpg').convert_alpha()
longest_road = pygame.image.load('resources/Top/longest_road.jpg').convert_alpha()


# aj work for the bank
bank = pygame.image.load('resources/Bank/bank.jpg').convert_alpha()

# Making the images smaller size
clay = pygame.transform.scale(Clay, (60, 100))
sheep = pygame.transform.scale(Sheep, (60, 100))
ore = pygame.transform.scale(Ore, (60, 100))
wood = pygame.transform.scale(Wood, (60, 100))
wheat = pygame.transform.scale(Wheat, (60, 100))

# aj work of scaling the images

cards_cards = pygame.transform.scale(cards_cards, (60, 40))
cities_cards = pygame.transform.scale(cities_cards, (60, 40))
development_cards = pygame.transform.scale(development_cards, (60, 40))
resource_cards = pygame.transform.scale(resource_cards, (60, 40))
road_cards = pygame.transform.scale(road_cards, (60, 40))
settlement = pygame.transform.scale(settlement, (60, 40))
victory_points = pygame.transform.scale(victory_points, (60, 40))

# for Top scaling
largest_army = pygame.transform.scale(largest_army, (100, 70))
longest_road = pygame.transform.scale(longest_road, (100, 70))


# for the bank
bank = pygame.transform.scale(bank, (60, 40))

# Mapping
#special_images = {
#    'largest_army': largest_army,
#    'longest_road': longest_road
#}


resource_images = {"clay": clay, "sheep": sheep, "ore": ore, "wood": wood, "wheat": wheat}

icon_images = {
    "cards_cards": cards_cards,
    "cities_cards": cities_cards,
    "development_cards": development_cards,
    "resource_cards": resource_cards,
    "road_cards": road_cards,
    "settlement": settlement,
    "victory_points": victory_points,
}

# Font for player instances
# Set the font size
font_size = 30
# Load the Pygame Serif font
font = pygame.font.Font(None, font_size)

# Game master instance
game_master = GameMaster()

# Load the images for the end turn button
end_turn_button_normal = pygame.image.load('resources/end_turn_button_normal.png').convert_alpha()
end_turn_button_hover = pygame.image.load('resources/end_turn_button_hover.png').convert_alpha()
# Makes the button smaller
end_turn_button_normal_small = pygame.transform.scale(end_turn_button_normal, (120, 80))
end_turn_button_hover_small = pygame.transform.scale(end_turn_button_hover, (120, 80))
# Create an instance of the Button class
end_turn_button = Button(890, 655, end_turn_button_normal_small, end_turn_button_hover_small)

# Load the images for the trade button
trade_button_normal = pygame.image.load('resources/trade_normal.png').convert_alpha()
trade_button_hover = pygame.image.load('resources/trade_button_hover.png').convert_alpha()
# Makes the button smaller
trade_button_normal_small = pygame.transform.scale(trade_button_normal, (120, 80))
trade_button_hover_small = pygame.transform.scale(trade_button_hover, (120, 80))
# Create an instance of the Button class
trade_button = Button(700, 655, trade_button_normal_small, trade_button_hover_small)


######################## Game Stage END #######################################################
four = [0,1,2,3]
#################### Game Stage Function ######################################################
def game():
    clock = pygame.time.Clock()
    running = True
    diceRolling = False  # boolean for event loop
    dRollCount = 0
    while running:
        screen.fill((79, 129, 189))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            ################################### THE DICE ANIMATION ##########################################
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseX, mouseY = pygame.mouse.get_pos()
                if (dice.d1X <= mouseX <= dice.d2X + dice.dimens) and (dice.d1Y <= mouseY <= dice.d1Y + dice.dimens)\
                    and not game_master.turn_inst.rolled and game_master.initialised:
                    if diceRolling == False:
                        pygame.time.set_timer(dice.EVENT, 100)
                        diceRolling = True  # so you can't retrigger dice roll when its already rolling
                        dRollCount = 0  # counting for an imation of dice roll

            elif event.type == dice.EVENT:
                if dRollCount == 10:  # num of seconds for animation x10
                    dRoll = dice.roll(screen)  # gets value of roll
                    game_master.turn_inst.set_roll(dRoll) #gives dice roll to turn class
                    game_master.pass_resources(sum(dRoll)) #doing this here might make above line redundant?
                    pygame.time.set_timer(dice.EVENT, 0)
                    diceRolling = False
                else:
                    dice.roll(screen)  # temp display of dice while rolling
                    dRollCount += 1
        ##########################################################################################################
        # display static dice when not rolling
        dice.display(screen)

        if quit_button2.draw(screen):
            running = False

        # board
        ui.main(screen, game_master)

        # Display the player's name and details
        game_master.turn_queue[0].display(screen, font, 10, SCREEN_HEIGHT - 320, resource_images)

        # aj work
        #  game_master.turn_queue[1].display_for_bots(screen, SCREEN_WIDTH - 300, 20, icon_images)
        #   game_master.turn_queue[2].display_for_bots(screen, SCREEN_WIDTH - 300, 320, icon_images)
        #  game_master.turn_queue[3].display_for_bots(screen, SCREEN_WIDTH - 300, 460, icon_images)
        game_master.turn_queue[1].display_for_bots(screen, SCREEN_WIDTH - 220, 20, icon_images)
        game_master.turn_queue[2].display_for_bots(screen, SCREEN_WIDTH - 400, 250, icon_images)
        game_master.turn_queue[3].display_for_bots(screen, SCREEN_WIDTH - 220, 350, icon_images)

        # bank display by aj
        #game_master.display_bank_image(screen, 100, 200, bank)

        #ame_master.display_bank(screen, 10, 20, icon_images, resource_images)

        # displays the number of turns so far and the current player's turn
        draw(game_master, screen)

        if end_turn_button.draw(screen):  # If the user clicks on the end_turn_button then...
            if game_master.turn_inst.rolled or not game_master.initialised:
                for i in four:
                    if game_master.turn_queue[i].check_if_over_ten():
                        running = False
                game_master.next_turn() #made more sense to me to put this after the win check

        if trade_button.draw(screen):  # If the user clicks on the trade_button then...
            print('Trading...')

        # crosshair
        crosshair_group.draw(screen)
        crosshair_group.update()
        #########################################################################
        # FPS
        clock.tick(60)
        pygame.display.flip()

############################# Main Game Loop #################################################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ####################################################################
    # buttons
    screen.blit(background, (0, 0))
    if start_button.draw(screen):
        game()
    if quit_button.draw(screen):
        running = False

    # crosshair
    crosshair_group.draw(screen)
    crosshair_group.update()
    crosshair.switch_image([start_button, quit_button])
    #########################################################################
    pygame.display.update()
# Quit Pygame
pygame.quit()
