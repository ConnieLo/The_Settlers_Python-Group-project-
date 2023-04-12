from unittest import TestCase

from classes.player import Player


class TestPlayer(TestCase):

    def setUp(self):
        self.test = Player("fin", "blue")
        self.test.resources = {"wood": 2, "brick": 1, "sheep": 0, "wheat": 4, "ore": 3}
        self.test.development_cards = {"Knights": 1, "Road Building": 0, "Year of Plenty": 0, "Monopoly": 2,
                                       "University": 0,
                                       "Market": 0, "Great Hall": 0, "Chapel": 0, "Library": 0, }

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
        self.test.add_development_cards("Knights", 1)

        # test value inside bound
        self.assertTrue(self.test.remove_development_cards("Knights", 2))

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
