import pygame
import random

class Card:
    def __init__(self, card_type, resources= None):
        self.card_type = card_type
        self.resources = resources or {}

    def __repr__(self):
        return self.card_type

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def create_deck(self):
        # Creates a deck of cards
        for i in range(14):
            self.cards.append(Card("Knight"))
        for i in range(5):
            self.cards.append(Card("Victory Point"))
        for i in range(2):
            self.cards.append(Card("Road Building"))
            self.cards.append(Card("Year of Plenty"))
            self.cards.append(Card("Monopoly"))
        random.shuffle(self.cards)

    def draw(self):
        # Draws a card from the deck and removes it from the deck
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

    def __len__(self):
        return len(self.cards)
