import unittest
from unittest import TestCase

from grid_structure import GridStruct


class TestGridBasic(unittest.TestCase):
    def test_set_get(self):
        pineapple = GridStruct()
        pineapple.set(0, 0, 1)  # Set a value at (0, 0)

        # Test getting a value within the grid bounds
        self.assertEqual(pineapple.get(0, 0), 1)

        # Test raising error if index out of bounds
        self.assertEqual(pineapple.get(100, 100), None)


