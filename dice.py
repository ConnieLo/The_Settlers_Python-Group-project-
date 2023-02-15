import networkx as nx
import random
import pygame

# VIEW dice_test FOR IMPLEMENTATION IN EVENT LOOP
class Dice:

    def __init__(self, x, y):
        self.face = ['diceFace1.png','diceFace2.png','diceFace3.png','diceFace4.png','diceFace5.png','diceFace6.png'] #array to hold images for dice faces
        self.d1X = x
        self.d1Y = y
        self.d2X = x+10+51 #10 pixel gap between dice and dice image size of 51x51, subject to change
        self.d2Y = y
        self.dimens = 51
        self.d1Val = 1
        self.d2Val = 1
        self.EVENT = pygame.USEREVENT + 1

    def num(self):
        return random.randint(1,6), random.randint(1,6) #randomises 2 dice rolls

    def roll(self):
        nums = self.num() #generates the result of a dice roll
        self.display(nums)
        self.d1Val = nums[0]
        self.d2Val = nums[1]
        return(nums)

    def display(self, nums = None):   #generate dice roll
        if nums == None:
            nums = [self.d1Val, self.d2Val]
        d1 = pygame.image.load(self.face[nums[0]-1]).convert()  #load dice 1
        d2 = pygame.image.load(self.face[nums[1]-1]).convert()  #load dice 2
        screen.blit(d1, (self.d1X, self.d1Y))   #'draw' dice 1
        screen.blit(d2, (self.d2X, self.d2Y))   #'draw' dice 2