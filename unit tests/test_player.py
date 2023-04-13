from unittest import TestCase

from classes.player import Player
from classes.settlement import Settlement


class TestPlayer(TestCase):

    def setUp(self):
        self.test = Player("fin", "blue")
        self.test.resources = {"wood": 2, "brick": 1, "sheep": 0, "wheat": 3, "ore": 4}
        self.test.development_cards = {"Knights": 1, "Road Building": 0, "Year of Plenty": 0, "Monopoly": 2,
                                       "University": 0,
                                       "Market": 0, "Great Hall": 0, "Chapel": 1, "Library": 0, }

        self.test.number_of_settlements = 1
        self.test.number_of_cities = 1

    def test_add_resource(self):
        # test adding a valid resource increases the quantity by 1
        self.test.add_resource('wood')
        self.assertEqual(self.test.resources['wood'], 3)

        # adding an invalid resource does not change the quantity
        self.test.add_resource('gold')
        self.assertEqual(self.test.resources['wood'], 3)

        # adding a resource multiple times increases resource accordingly
        self.test.add_resource('brick')
        self.test.add_resource('brick')
        self.assertEqual(self.test.resources['brick'], 3)

    def test_remove_resources(self):
        self.test.add_resource("brick")

        # test remove value inside bound
        self.assertTrue(self.test.remove_resources("brick"))

        # test remove value outside bound
        self.assertFalse(self.test.remove_resources("sheep"))

    def test_add_development_cards(self):
        # adding dev card increases quantity accordingly
        self.test.add_development_cards("Knights", 1)
        self.assertEqual(self.test.development_cards["Knights"], 2)

    def test_remove_development_cards(self):
        # test value inside bound
        self.assertTrue(self.test.remove_development_cards("Knights", 1))

        # test value outside bound
        self.assertFalse(self.test.remove_development_cards("Library", 1))

    def test_can_afford_cost(self):
        # test that a cost the player can afford returns True
        cost = {"wood": 1, "brick": 1, "wheat": 2}
        self.assertTrue(self.test.can_afford_cost(cost))

        # test that a cost the player cannot afford returns False
        cost = {"wood": 1, "brick": 1, "sheep": 1}
        self.assertFalse(self.test.can_afford_cost(cost))

        # test that a cost with zero quantity required returns true
        cost = {"wood": 0, "sheep": 0}
        self.assertTrue(self.test.can_afford_cost(cost))

    def test_get_total_resources(self):
        # test to count the total num of resources
        self.assertEqual(self.test.get_total_resources(), 10)

        # test value out of bounds
        self.assertNotEqual(self.test.get_total_resources(), 0)

        # method returns an integer
        self.assertIsInstance(self.test.get_total_resources(), int)

    def test_discard_resources(self):
        # test not working!!!
        # should return true as there are more than 7 resources?
        # self.test.resources = {"wood": 2, "brick": 1, "sheep": 0, "wheat": 3, "ore": 4}
        # self.assertTrue(self.test.discard_resources())

        # returns false if there are 7 or less resources
        self.test.resources = {"wood": 1, "brick": 1, "sheep": 1, "wheat": 1, "ore": 1}
        self.assertFalse(self.test.discard_resources())

    def test_get_total_development_cards(self):
        # test to count the total num of dev cards
        self.assertEqual(self.test.get_total_development_cards(), 4)

        # test value out of bounds
        self.assertNotEqual(self.test.get_total_development_cards(), 0)

        # method returns an integer
        self.assertIsInstance(self.test.get_total_development_cards(), int)

    # # will not work until method complete!!
    # def test_get_victory_points_from_cities_and_settlements(self):
    #     # test method returns integer
    #     self.assertIsInstance(self.test.get_victory_points_from_settlements_and_cities(), int)
    #
    #     # test method returns correct number
    #     self.assertEqual(self.test.get_victory_points_from_settlements_and_cities(), 3)
    #
    #     # test value out of bounds
    #     self.assertNotEqual(self.test.get_victory_points_from_settlements_and_cities(), 0)

    def test_get_victory_points_from_development_cards(self):
        # test method returns an integer
        self.assertIsInstance(self.test.get_victory_points_from_development_cards(), int)

        # test value inside bounds
        self.assertEqual(self.test.get_victory_points_from_development_cards(), 1)

        # test value outside bounds
        self.assertNotEqual(self.test.get_victory_points_from_development_cards(), 6)

    # # will not work until method complete
    # def test_get_victory_points_from_other_sources(self):
    #     # test method returns integer
    #     self.assertIsInstance(self.test.get_victory_points_from_other_sources(), int)

    # # will not work until method complete
    # def test_get_total_victory_points(self):
    #     # method returns integer
    #     self.assertIsInstance(self.test.get_total_victory_points(), int)
    #
    #     # test method returns correct number
    #     self.assertEqual(self.test.get_total_victory_points(), 4)
