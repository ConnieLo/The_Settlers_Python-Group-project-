import random

import pygame

from classes import DevelopmentCard, settlement, trade
from classes.trade import Trade


class Player:
    """
    A player object exists for every player in the game, whether human or bot controlled.

    ATTRIBUTES

    name: str
        A string representing the name of this player

    colour: collection
        The colour this player is represented by on-screen,
        stored as a standard RBG value in a 3-element collection.

    score: int
        The number of victory points this player has

    resources: dict
        The number of resource cards of each type this player has,
        stored as a map where the key is the name of the resource as a string e.g. “clay”.
        By convention, these names are lower case

    development_cards: dict
        The number of development cards the player has available to them.
        Stored as a map where the key is the name of the card as a string e.g. “Year of Plenty”.
        By convention, these names are title case.

    number_of_roads: int
        The number of roads this player has

    number_of_settlements: int
        The number of settlements this player has

    number_of_cities: int
        The number of cities this player has

    initialised: bool
        To check if player has placed their first 2 settlements and roads
    """

    def __init__(self, name, color, bot_number=None):
        self.name = name
        self.color = color
        self.bot_number = bot_number  # add by aj
        self.score = 0
        self.resources = {"wood": 0, "clay": 0, "sheep": 0, "wheat": 0, "ore": 0}
        self.development_cards = {"Knights": 0, "Road Building": 0, "Year of Plenty": 0, "Monopoly": 0, "University": 0,
                                  "Market": 0, "Great Hall": 0, "Chapel": 0, "Library": 0, }
        self.number_of_roads = 0
        self.number_of_settlements = 0
        self.number_of_cities = 0
        self.initialised = False

    def add_resource(self, resource_type: str):
        """
        Increments the resource of the given type by 1
        :param resource_type: str
            the type of resource
        """
        if resource_type in self.resources:
            self.resources[resource_type] += 1

    def remove_resources(self, resource: str, quantity: int =1) -> bool:
        """
        Removes the given number of the given resource, if the player has them, and returns true.
        If the player does not have enough, or any, of the given resource, nothing is changed

        :param resource: str
            The type of resource
        :param quantity:
            The amount
        :return: True if any resources taken
        """
        if self.resources[resource] >= quantity:
            self.resources[resource] -= quantity
            return True
        else:
            return False

    def increment_victory_points(self, points=1):
        """
        Increments the victory points 1, or the given number
        :param points: int, optional
            The number of points. Default 1
        """
        self.score += points

    def increment_number_of_settlements(self):
        """Increments the settlement number by 1."""
        self.number_of_settlements += 1

    def increment_number_of_roads(self):
        """Increments the road number by 1."""
        self.number_of_roads += 1

    def add_development_cards(self, development_cards, quantity=1):
        """
        Grants a single (or multiple, if specified) development card of the given type
        :param development_cards: str
            The type of development card
        :param quantity: int, optional
            The amount. Default 1
        """
        self.development_cards[development_cards] += quantity

    def remove_development_cards(self, development_cards, quantity=1):
        """
        Discards a single (or multiple, if specified) development card of the given type
        :param development_cards: str
            The type of development card
        :param quantity: int, optional
            The amount. Default 1
        """
        # changed self.resources to self.development_cards
        if self.development_cards[development_cards] >= quantity:
            self.development_cards[development_cards] -= quantity
            return True
        else:
            return False

    def check_enough_res_settle(self) -> bool:
        """
        checks if the player has enough resources to build a settlement
        :return True if they have enough
        """
        if self.resources["wood"] >= 1 and self.resources["clay"] >= 1 and self.resources["sheep"] >= 1 and \
                self.resources["wheat"] >= 1:
            return True
        else:
            return False

    def check_enough_res_road(self) -> bool:
        """
        checks if the player has enough resources to build a road
        :return True if they have enough
        """
        print("allo")
        if self.resources["clay"] >= 1 and self.resources["wood"] >= 1:
            return True
        else:
            return False

    def purchase_road(self):
        """Discards resources equal to the cost of one road"""
        road_cost = [("wood", 1), ("clay", 1)]
        for res, quan in road_cost:
            self.remove_resources(res, quan)

    def purchase_settle(self):
        """Discards resources equal to the cost of one settlement"""
        settle_cost = [("wood", 1), ("clay", 1), ("sheep", 1), ("wheat", 1)]
        for res, quan in settle_cost:
            self.remove_resources(res, quan)

    def can_afford_cost(self, cost):
        """
        checks if the player has enough resources to pay a given cost.
        :param cost: dict
            Given as {resource: amount} pairs
        """
        for resource, quantity in cost.items():
            if self.resources.get(resource, 0) < quantity:
                return False
        return True

    def buy_development_card(self, deck):
        """
        Allows the player to purchase a development card from a given deck
        :param deck: Deck
            The deck from which to draw
        """
        card = deck.draw()
        if card and self.can_afford_cost(card.cost):
            self.development_cards[card.name] += 1
            for resource, quantity in card.cost.items():
                self.remove_resources(resource, quantity)
            return True
        return False

    def play_development_card(self, card):
        """
        UNIMPLEMENTEDED
        This method allows the player to play a development card from their hand.

        :param card: DevelopmentCard
            The card to play
        """
        # if self.development_cards[card] > 0:
        pass

    def trade_resources_with_bank(self, give, receive):
        """
        Allows the player to trade a specified amount of resources with the bank
        :param give: str
            The outgoing resource
        :param receive: str
            The incoming resource
        """
        trade_ratios = {"wood": 4, "brick": 4, "sheep": 4, "wheat": 4, "ore": 4}
        if self.resources[give] >= trade_ratios[give]:
            self.resources[give] -= trade_ratios[give]
            self.resources[receive] += 1
            return True  # Trade successful
        else:
            return False  # Player does not have enough resources to make the trade

    def trade_resources_with_player(self, other_player, give, receive):
        """
        Allows the player to trade a specified amount of resources with another player
        :param other_player
            The other party in the trade
        :param give: str
            The outgoing resource
        :param receive: str
            The incoming resource
        """
        trade = Trade(self, other_player, give, receive)
        return trade.execute()

    def discard_resources(self):
        """
        Forces the player to discard resources if they have more than 7 cards in their hand during
        the game's resource production phase
        """
        # Get the total number of resources in the player's hand
        num_resources = self.get_total_resources()
        # If the player has 7 or fewer resources, they do not need to discard any
        if num_resources <= 7:
            return False  # Player does not need to discard resources
        else:  # Determine how many resources the player needs to discard
            num_to_discard = num_resources // 2
            # Create a list of resources that can be discarded
            resources_to_discard = []
            for resource, count in self.resources.items():
                if count > num_to_discard:
                    resources_to_discard.extend([resource] * (count - num_to_discard))
            # If there are not enough resources that can be discarded, the player cannot discard enough
            if len(resources_to_discard) < num_to_discard:
                return False  # Player cannot discard enough resources
            else:
                for i in range(
                        num_to_discard):  # Randomly select resources to discard until the correct number have been discarded
                    resource_to_remove = random.choice(resources_to_discard)
                    self.resources[resource_to_remove] -= 1
                    resources_to_discard.remove(resource_to_remove)
                return True  # Player has successfully discarded resources

    def get_total_resources(self) -> int:
        """
        Returns the number of resource cards in the players hand
        :return The number of resources
        """
        total = 0
        for resource, quantity in self.resources.items():
            total += quantity
        return total

    def get_total_development_cards(self):
        """
        Returns the number of development cards in the players hand
        :return The number of development cards
        """
        total = 0
        for card, quantity in self.development_cards.items():
            total += quantity
        return total

    def get_victory_points_from_settlements_and_cities(self) -> int:
        """
        Calculates the number of victory points the player has from their settlements and cities
        :return The amount of victory points
        """
        settlements_and_cities = self.get_settlements_or_cities_on_vertex()
        return settlements_and_cities.count("Settlement") + 2 * settlements_and_cities.count("City")

    def get_victory_points_from_development_cards(self):
        """
        Calculates the number of victory points the player has from their development cards
        :return The amount of victory points
        """
        return self.development_cards["University"] + self.development_cards["Great Hall"] + \
               self.development_cards["Chapel"] + self.development_cards["Library"]

    def get_victory_points_from_other_sources(self):
        """
        Calculates the number of victory points the player has from other sources,
        such as having the longest road or largest army
        :return The amount of victory points
        """
        return self.get_longest_road_length() + self.get_largest_army_size()

    def get_total_victory_points(self):
        """
        Calculates the total number of victory points the player has
        :return The amount of victory points
        """
        self.score += self.get_victory_points_from_settlements_and_cities() + \
                      self.get_victory_points_from_development_cards() + self.get_victory_points_from_other_sources()
        return self.score

    def check_if_over_ten(self) -> bool:
        """Returns true if the player has 10 OR MORE victory points"""
        if self.score >= 10:
            return True
        else:
            return False

    # TODO
    def prompt_trade(self):
        """
        UNIMPLEMENTED TODO
        Notifies the player to make trade requests for that turn
        """
        pass

    # TODO
    def prompt_builds(self):
        """
        UNIMPLEMENTED TODO
        Notifies the player to build roads and settlements for that turn
        """
        pass

    def display(self, surface, font, x, y, resource_images):
        """
        Intended for the player controlled by the user.

        Constructs and renders a visually intuitive display with details about the player's current state,
        including: how many of each resource they have, which development cards they have, how many
        victory points they have so far achieved etc.

        :param surface: The Pygame surface on which to draw the display
        :param font: The Pygame font to use
        :param x: X co-ordinate at which to draw the display
        :param y: Y co-ordinate at which to draw the display
        :param resource_images: The images to be used for the resources
        """
        text = font.render(f"{self.name}'s Victory Points: {self.score}", True, self.color)
        surface.blit(text, (x, y))

        resource_y_offset = 50
        resource_x_offset = 0
        for resource, image in resource_images.items():  # Extraction of resource_images list
            surface.blit(image, (x + resource_x_offset, y + resource_y_offset))  # Blits the images
            count_text = font.render(str(self.resources[resource]), True, self.color)
            text_width, _ = count_text.get_size()
            count_x_offset = (
                                     image.get_width() - text_width) // 2  # This value is used to move the numbers to the center of the corresponding image
            vertical_offset = 10  # This value is used to move the numbers further down
            # Adds up all the offsets for the numbers text
            surface.blit(count_text, (
                x + resource_x_offset + count_x_offset, y + resource_y_offset + image.get_height() + vertical_offset))
            resource_x_offset += image.get_width() + 20

        # text3 = font.render(f"Development Cards: {self.development_cards}", True, self.color)
        # surface.blit(text3, (x, y + resource_y_offset + image.get_height() + 50))

        text5 = font.render(f"Number of Settlements: {self.number_of_settlements}", True, self.color)
        surface.blit(text5, (x, y + resource_y_offset + image.get_height() + 60))

        text4 = font.render(f"Number of Roads: {self.number_of_roads}", True, self.color)
        surface.blit(text4, (x, y + resource_y_offset + image.get_height() + 100))

        text5 = font.render(f"Number of Cities: {self.number_of_cities}", True, self.color)
        surface.blit(text5, (x, y + resource_y_offset + image.get_height() + 140))

        """
        Intended for players controlled by bots or humans other than the user.

        Constructs and renders a visually intuitive display with details about the player's current state,
        including: how many of each resource they have, which development cards they have, how many
        victory points they have so far achieved etc.

        :param surface: The Pygame surface on which to draw the display
        :param x: X co-ordinate at which to draw the display
        :param y: Y co-ordinate at which to draw the display
        :param icon_images: #TODO
        """

    def display_for_bots(self, surface, x, y, icon_images, resource_images):
        icon_y_offset = 0
        extra_spacing = 770  # Increase this value to add more space between players

        info = [
            {"text": f"{self.name}", "icon": None},
            {"text": f"VP: {self.score}", "icon": "victory_points"},
            {"text": None, "icon": None, "display_resources": True},
            {"text": f"Dev Cards: {sum(self.development_cards.values())}", "icon": "development_cards"},
            {"text": f"Roads: {self.number_of_roads}", "icon": "road_cards"},
            {"text": f"Cities: {self.number_of_cities}", "icon": "cities_cards"},
        ]

        font = pygame.font.Font(None, 24)

        for item in info:
            if item["icon"]:
                icon = icon_images[item["icon"]]
                surface.blit(icon, (x, y + icon_y_offset))

            if item["text"]:
                text = font.render(item["text"], True, self.color)
                text_width, text_height = text.get_size()
                text_x_offset = (icon.get_width() if item["icon"] else 0) + 5

                surface.blit(text, (x + text_x_offset, y + icon_y_offset))

            if item.get("display_resources"):
                resource_y_offset = icon_y_offset
                resource_x_offset = 0
                for resource, image in resource_images.items():  # Extraction of resource_images list
                    # Scaling down the images
                    scaled_image = pygame.transform.scale(image, (image.get_width() // 2, image.get_height() // 2))

                    surface.blit(scaled_image, (x + resource_x_offset, y + resource_y_offset))  # Blits the images
                    count_text = font.render(str(self.resources[resource]), True, self.color)
                    text_width, _ = count_text.get_size()
                    count_x_offset = (
                        scaled_image.get_width() - text_width) // 2  # This value is used to move the numbers to the center of the corresponding image
                    vertical_offset = 10  # This value is used to move the numbers further down
                    # Adds up all the offsets for the numbers text
                    surface.blit(count_text, (
                        x + resource_x_offset + count_x_offset, y + resource_y_offset + scaled_image.get_height() + vertical_offset))
                    resource_x_offset += scaled_image.get_width() + 20
                icon_y_offset += scaled_image.get_height() + 40  # Increased space between icons and card images
            elif item["icon"]:
                icon_y_offset += max(icon.get_height(), text_height) + 5
            else:
                icon_y_offset += text_height + 5

        icon_y_offset += extra_spacing

    def card_select_resource(self):
        """
        TODO Should prompt either the bot or ui to select a resource for a development card action
        as it exists now, just returns wood
        :return: a resource
        """
        return "wood"
