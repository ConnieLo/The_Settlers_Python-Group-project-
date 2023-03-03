import pygame
import cards
import settlement
import vertex
import trade

class player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0
        self.resources = {"wood": 0, "brick": 0, "sheep": 0, "wheat": 0, "ore": 0}
        self.development_cards = {"Knights": 0, "Road Building": 0, "Year of Plenty": 0, "Monopoly": 0, "University": 0, "Market": 0, "Great Hall": 0, "Chapel": 0, "Library": 0,}

    def add_resources(self, resource, quantity):
        self.resources[resource] += quantity

    def remove_resources(self, resource, quantity):
        if self.resources[resource] >= quantity:
            self.resources[resource] -= quantity
            return True
        else:
            return False

    #def reset_resources(self): #redundant at the momemnt
    #    self.resources = {"wood": 0, "brick": 0, "sheep": 0, "wheat": 0, "ore": 0}

    def add_development_cards(self, development_cards, quantity):
        self.development_cards[development_cards] += quantity

    def remove_development_cards(self, development_cards, quantity):
        if self.resources[development_cards] >= quantity:
            self.resources[development_cards] -= quantity
            return True
        else:
            return False

    def new_settlement(self, vertex):
        vertex.add_settlement(self)

    def add_city(self, vertex):
        # This method upgrades an existing settlement to a city at a given vertex.
        vertex.add_city(self)

    def build_road(self, edge):
        # This method builds a new road at a given edge on the game board.
        edge.build_road(self)

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

    def play_development_card(self, card):
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
        else: # Determine how many resources the player needs to discard
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
                for i in range(num_to_discard): # Randomly select resources to discard until the correct number have been discarded
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

    def display(self, surface, font, x, y):
        text = font.render(f"{self.name}'s Victory Points: {self.score}", True, self.color)
        text2 = font.render(f"{self.name}'s Resources: {self.resources}", True, self.color)
        text3 = font.render(f"{self.name}'s Development Cards: {self.development_cards}", True, self.color)
        surface.blit(text, (x, y))
        surface.blit(text2, (x, y+50))
        surface.blit(text3, (x, y+80))