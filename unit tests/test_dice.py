from unittest import TestCase

import unittest

from classes.dice import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice(0, 0, 51)

    # Test if the Dice class is initialized correctly with the provided values.
    def test_initialization(self):
        self.assertEqual(self.dice.d1X, 0)
        self.assertEqual(self.dice.d1Y, 0)
        self.assertEqual(self.dice.size, 51)
        self.assertEqual(self.dice.d2X, 61)
        self.assertEqual(self.dice.d2Y, 0)
        self.assertEqual(self.dice.dimens, 51)
        self.assertEqual(self.dice.d1Val, 1)
        self.assertEqual(self.dice.d2Val, 1)

    # Test if the num() method generates two random numbers between 1 and 6, inclusive.
    def test_num(self):
        nums = self.dice.num()
        self.assertTrue(1 <= nums[0] <= 6)
        self.assertTrue(1 <= nums[1] <= 6)

    # Test if the roll() method generates two random numbers between 1 and 6, inclusive.
    def test_roll(self):
        nums = self.dice.roll(None)
        self.assertTrue(1 <= nums[0] <= 6)
        self.assertTrue(1 <= nums[1] <= 6)


if __name__ == '__main__':
    unittest.main()
#
# class TestDice(TestCase):
#     def test_num(self):
#         self.fail()
#
#     def test_roll(self):
#         self.fail()
#
#     def test_display(self):
#         self.fail()
######################################once i make changes to the dice class####################################################
#
#
# import unittest
#
# class TestDice(unittest.TestCase):
#
#     def setUp(self):
#         self.dice = Dice(0, 0, 51)
#
#     def test_initialization(self):
#         self.assertEqual(self.dice.d1X, 0)
#         self.assertEqual(self.dice.d1Y, 0)
#         self.assertEqual(self.dice.size, 51)
#         self.assertEqual(self.dice.d2X, 61)
#         self.assertEqual(self.dice.d2Y, 0)
#         self.assertEqual(self.dice.dimens, 51)
#         self.assertEqual(self.dice.d1Val, 1)
#         self.assertEqual(self.dice.d2Val, 1)
#
#     def test_num(self):
#         nums = self.dice.num()
#         self.assertTrue(1 <= nums[0] <= 6)
#         self.assertTrue(1 <= nums[1] <= 6)
#
#     def test_roll(self):
#         nums = self.dice.roll(None)
#         self.assertTrue(1 <= nums[0] <= 6)
#         self.assertTrue(1 <= nums[1] <= 6)
#
#     def test_load_image(self):
#         image = self.dice.load_image(1)
#         self.assertIsInstance(image, pygame.Surface)
#
#     def test_scale_image(self):
#         original_image = self.dice.load_image(1)
#         scaled_image = self.dice.scale_image(original_image)
#         self.assertEqual(scaled_image.get_width(), self.dice.size)
#         self.assertEqual(scaled_image.get_height(), self.dice.size)
#


##################this is how i feel the Dice class can be #######################

#
# import random
# import pygame
#
# class Dice:
#
#     def __init__(self, x, y, size):
#         self.face = [
#             'resources/dice/diceOne.png',
#             'resources/dice/diceTwo.png',
#             'resources/dice/diceThree.png',
#             'resources/dice/diceFour.png',
#             'resources/dice/diceFive.png',
#             'resources/dice/diceSix.png'
#         ]
#         self.d1X = x
#         self.d1Y = y
#         self.size = size
#         self.d2X = x + 10 + 51
#         self.d2Y = y
#         self.dimens = 51
#         self.d1Val = 1
#         self.d2Val = 1
#         self.EVENT = pygame.USEREVENT + 1
#
#     def num(self):
#         return random.randint(1, 6), random.randint(1, 6)
#
#     def load_image(self, face_number):
#         return pygame.image.load(self.face[face_number - 1]).convert()
#
#     def scale_image(self, image):
#         return pygame.transform.scale(image, (self.size, self.size))
#
#     def roll(self, screen):
#         nums = self.num()
#         self.display(screen, nums)
#         self.d1Val = nums[0]
#         self.d2Val = nums[1]
#         return nums
#
#     def display(self, screen, nums=None):
#         if nums == None:
#             nums = [self.d1Val, self.d2Val]
#         d1 = self.load_image(nums[0])
#         d2 = self.load_image(nums[1])
#         d1 = self.scale_image(d1)
#         d2 = self.scale_image(d2)
#         screen.blit(d1, (self.d1X, self.d1Y))
#         screen.blit(d2, (self.d2X, self.d2Y))
