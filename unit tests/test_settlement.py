from unittest import TestCase

from classes.settlement import Settlement


# Dummy Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {
            'wood': 0,
            'brick': 0,
            'ore': 0,
            'wheat': 0,
            'sheep': 0
        }

    def add_resource(self, resource):
        self.resources[resource] += 1


# Test cases for Settlement class
class TestSettlement(TestCase):

    def setUp(self):
        self.player = Player('tom')
        self.settlement_info = [(5, 'wood'), (8, 'brick'), (9, 'ore')]
        self.settlement = Settlement(self.player, self.settlement_info)

    # Test if the Settlement class is initialized correctly with the provided values.
    def test_initialization(self):
        self.assertEqual(self.settlement.owner, self.player)
        self.assertEqual(self.settlement.is_city, False)
        self.assertEqual(self.settlement.settlement_info, self.settlement_info)

    # Test if the grant_resources() method adds the correct resources to the player when a matching number is given.
    def test_grant_resources(self):
        self.settlement.grant_resources(5)
        self.assertEqual(self.player.resources['wood'], 1)

        self.settlement.grant_resources(8)
        self.assertEqual(self.player.resources['brick'], 1)

        self.settlement.grant_resources(9)
        self.assertEqual(self.player.resources['ore'], 1)

    # Test if the grant_resources() method does not add any resources to the player when a non-matching number is given.
    def test_no_resources_granted(self):
        self.settlement.grant_resources(4)
        for resource in self.player.resources.values():
            self.assertEqual(resource, 0)

    # Test if the grant_resources() method adds multiple resources to the player when multiple matching numbers are
    # given.
    def test_grant_multiple_resources(self):
        self.settlement.settlement_info.append((5, 'wood'))
        self.settlement.grant_resources(5)
        self.assertEqual(self.player.resources['wood'], 2)

    # def test_grant_resources(self):
    #     self.fail()
