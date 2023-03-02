import pygame
import cards
import settlement
import vertex

class player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0
        self.resources = {"wood": 0, "brick": 0, "sheep": 0, "wheat": 0, "ore": 0}
        self.development_cards = {"Knights": 0, "Road Building": 0, "Year of Plenty": 0, "Monopoly": 0, "University": 0, "Market": 0, "Great Hall": 0, "Chapel": 0, "Library": 0,}

    def increase_score(self, points):
        self.score += points

    def add_resources(self, resource, quantity):
        self.resources[resource] += quantity

    def remove_resources(self, resource, quantity):
        if self.resources[resource] >= quantity:
            self.resources[resource] -= quantity
            return True
        else:
            return False

    def reset_resources(self):
        self.resources = {"wood": 0, "brick": 0, "sheep": 0, "wheat": 0, "ore": 0}

    def display(self, surface, font, x, y):
        text = font.render(f"{self.name}'s Victory Points: {self.score}", True, self.color)
        text2 = font.render(f"{self.name}'s Resources: {self.resources}", True, self.color)
        text3 = font.render(f"{self.name}'s Development Cards: {self.development_cards}", True, self.color)
        surface.blit(text, (x, y))
        surface.blit(text2, (x, y+50))
        surface.blit(text3, (x, y+80))

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

