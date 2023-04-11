import pygame
import random

class DevelopmentCard:
    def __init__(self, card_type, resources= None):
        self.card_type = card_type
        self.resources = resources or {}

    def __repr__(self):
        return self.card_type

class Deck:
    def __init__(self):
        self.DevelopmentCards = []
        self.create_deck()

    def create_deck(self):
        # Creates a deck of cards
        for i in range(14):
            self.DevelopmentCards.append(DevelopmentCard("Knight"))
        for i in range(5):
            self.DevelopmentCards.append(DevelopmentCard("Victory Point"))
        for i in range(2):
            self.DevelopmentCards.append(DevelopmentCard("Road Building"))
            self.DevelopmentCards.append(DevelopmentCard("Year of Plenty"))
            self.DevelopmentCards.append(DevelopmentCard("Monopoly"))
        random.shuffle(self.DevelopmentCards)

    def draw(self):
        # Draws a card from the deck and removes it from the deck
        if len(self.DevelopmentCards) > 0:
            return self.DevelopmentCards.pop()
        else:
            return None

    def __len__(self):
        return len(self.DevelopmentCards)
