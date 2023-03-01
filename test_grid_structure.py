import unittest
from unittest import TestCase

from grid_structure import GridBasic


class TestGridBasic(unittest.TestCase):
    def test_set_get(self):
        self._grid = GridBasic()
        self._grid.set(0, 0, 1)  # Set a value at (0, 0)

        # Test getting a value within the grid bounds
        self.assertEqual(self._grid.get(0, 0), 1)

        # Test getting a value outside the grid bounds
        self.assertEqual(self._grid.get(0, 1), 0)

        # Test raising error if index out of bounds
        with self.assertRaises(IndexError):
            self._grid.get(10, 10)


