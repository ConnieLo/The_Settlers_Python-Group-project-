import random

import pygame


class Player:
    def __init__(self, name, color, bot_number=None):
        self.name = name
        self.color = color
        self.bot_number = bot_number  # add by aj
        self.score = 0
        self.resources = {"wood": 0, "brick": 0, "sheep": 0, "wheat": 0, "ore": 0}
        self.development_cards = {"Knights": 0, "Road Building": 0, "Year of Plenty": 0, "Monopoly": 0, "University": 0,
                                  "Market": 0, "Great Hall": 0, "Chapel": 0, "Library": 0, }
        self.number_of_roads = 0
        self.number_of_settlements = 0
        self.number_of_cities = 0
        self.number_of_cards = 0

    def add_resource(self, resource_type):
        print("Adding {} to {}".format(resource_type, self.name))
        if resource_type in self.resources:
            self.resources[resource_type] += 1

    def remove_resources(self, resource, quantity=1):
        if self.resources[resource] >= quantity:
            self.resources[resource] -= quantity
            return True
        else:
            return False

    def increment_victory_points(self, points=1):
        self.score += points

    # def reset_resources(self): # Redundant at the momemnt
    #    self.resources = {"wood": 0, "brick": 0, "sheep": 0, "wheat": 0, "ore": 0}

    def add_development_cards(self, development_cards, quantity):
        self.development_cards[development_cards] += quantity

    def remove_development_cards(self, development_cards, quantity):
        # changed this from self.resources to self.development cards
        if self.development_cards[development_cards] >= quantity:
            self.development_cards[development_cards] -= quantity
            return True
        else:
            return False

    def get_longest_road_length(self):
        # This method calculates the length of the longest road the player currently has on the game board.
        # we may use depth first search here
        pass

    def get_largest_army_size(self):
        # This method calculates the size of the largest army the player currently has on the game board.
        pass

    def can_afford_cost(self, cost):
        # This method checks if the player has enough resources to pay a given cost.
        for resource, quantity in cost.items():
            if self.resources[resource] < quantity:
                return False
        return True

    def buy_development_card(self, deck):
        # This method allows the player to purchase a development card from a given deck.
        card = deck.draw()
        if card and self.can_afford_cost(card.cost):
            self.development_cards[card.name] += 1
            for resource, quantity in card.cost.items():
                self.remove_resources(resource, quantity)
            return True
        return False

    def play_development_card(self, card):  # Maybe in the wrong class
        # This method allows the player to play a development card from their hand.
        # if self.development_cards[card] > 0:
        pass

    def trade_resources_with_bank(self, give, receive):
        # This method allows the player to trade a specified amount of resources with the bank.
        trade_ratios = {"wood": 4, "brick": 4, "sheep": 4, "wheat": 4, "ore": 4}
        if self.resources[give] >= trade_ratios[give]:
            self.resources[give] -= trade_ratios[give]
            self.resources[receive] += 1
            return True  # Trade successful
        else:
            return False  # Player does not have enough resources to make the trade

    def trade_resources_with_player(self, other_player, give, receive):
        # This method allows the player to trade a specified amount of resources with another player.
        trade = Trade(self, other_player, give, receive)
        return trade.execute()

    def discard_resources(self):
        # This method allows the player to discard resources if they have more than 7 cards in their hand during the game's resource production phase.
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

    def get_total_resources(self):
        total = 0
        for resource, quantity in self.resources.items():
            total += quantity
        return total

    def get_total_development_cards(self):
        total = 0
        for card, quantity in self.development_cards.items():
            total += quantity
        return total

    def has_settlements_or_cities_on_vertex(self, vertex):
        # This method checks if the player has any settlements or cities on a given vertex.
        # this needs data structure in order for this method to be implemented
        pass

    def get_settlements_or_cities_on_vertex(self, vertex):
        # This method returns the number of settlements and cities the player has on a given vertex.
        # this needs data structure in order for this method to be implemented
        pass

    def get_victory_points_from_settlements_and_cities(self):
        # This method calculates the number of victory points the player has from their settlements and cities.
        settlements_and_cities = self.get_settlements_or_cities_on_vertex()
        return settlements_and_cities.count("Settlement") + 2 * settlements_and_cities.count("City")

    def get_victory_points_from_development_cards(self):
        # This method calculates the number of victory points the player has from their development cards.
        return self.development_cards["University"] + self.development_cards["Great Hall"] + \
            self.development_cards["Chapel"] + self.development_cards["Library"]

    def get_victory_points_from_other_sources(self):
        # This method calculates the number of victory points the player has from other sources, such as having the longest road or largest army.
        return self.get_longest_road_length() + self.get_largest_army_size()

    def get_total_victory_points(self):
        # This method calculates the total number of victory points the player has.
        self.score += self.get_victory_points_from_settlements_and_cities() + \
                      self.get_victory_points_from_development_cards() + self.get_victory_points_from_other_sources()
        return self.score

    # TODO
    def prompt_trade(self):
        pass

    # TODO
    def prompt_builds(self):
        pass

    def display(self, surface, font, x, y, resource_images, special_images, players):
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

        largest_army = special_images['largest_army']
        longest_road = special_images['longest_road']

        largest_army_pos = (750, 20)
        longest_road_pos = (400 + largest_army.get_width() + 20, 20)

        if self.has_largest_army(players):
            surface.blit(largest_army, largest_army_pos)
        else:
            surface.blit(largest_army, largest_army_pos)  # Display image regardless of condition

        if self.has_longest_road(players):
            surface.blit(longest_road, longest_road_pos)
        else:
            surface.blit(longest_road, longest_road_pos)  # Display image regardless of condition



    def display_for_bots(self, surface, x, y, icon_images):
        icon_y_offset = 0
        extra_spacing = 770  # Increase this value to add more space between players

        info = [
            {"text": f"{self.name}", "icon": None},
            {"text": f"VP: {self.score}", "icon": "victory_points"},
            {"text": f"RC: {sum(self.resources.values())}", "icon": "resource_cards"},
            {"text": f"DC: {sum(self.development_cards.values())}", "icon": "development_cards"},
            {"text": f"Roads: {self.number_of_roads}", "icon": "road_cards"},
            {"text": f"Cities: {self.number_of_cities}", "icon": "cities_cards"},
            {"text": f"Cards: {self.number_of_cards}", "icon": "cards_cards"},
        ]

        font = pygame.font.Font(None, 24)

        for item in info:
            if item["icon"]:
                icon = icon_images[item["icon"]]
                surface.blit(icon, (x, y + icon_y_offset))

            text = font.render(item["text"], True, self.color)
            text_width, text_height = text.get_size()
            text_x_offset = (icon.get_width() if item["icon"] else 0) + 5

            surface.blit(text, (x + text_x_offset, y + icon_y_offset))

            if item["icon"]:
                icon_y_offset += max(icon.get_height(), text_height) + 5
            else:
                icon_y_offset += text_height + 5

        icon_y_offset += extra_spacing

    def has_largest_army(self, players):
        if self.development_cards['Knights'] >= 3:
            for player in players:
                if player != self and player.development_cards['Knights'] >= self.development_cards['Knights']:
                    return False
            return True
        return False

    def has_longest_road(self, players):
        longest_road_length = self.get_longest_road_length()

        if longest_road_length is None or longest_road_length < 5:
            return False

        for player in players:
            if player != self and player.get_longest_road_length() >= longest_road_length:
                return False

        return True

