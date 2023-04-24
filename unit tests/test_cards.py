from unittest import TestCase
from classes import game_master, player, dev_card_manager
import unittest

class TestCards(unittest.TestCase):

    def setup(self):
        self.master = game_master.GameMaster()
        self.players = self.master.turn_queue