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

    def test_get_set_vertex(self):
        banana = GridStruct()
        banana._set_vertex(0, 0, 0, 'v')
        banana._set_vertex(0, 1, 3, 'v')

        # test value inside bounds
        self.assertEqual(banana._get_vertex(0, 0, 0), banana._get_vertex(0, 1, 3))

        # test wrong value
        self.assertEqual(banana._get_vertex(0, 0, 0), 'e')

        # test value outside bounds
        self.assertEqual(banana._get_vertex(0, 0, 0), banana._get_vertex(1, 1, 1))

    def test_get_set_edge(self):
        mango = GridStruct()
        mango._set_edge(0, 0, 2, 'e')
        mango._set_edge(1, 0, 5, 'e')

        # test value inside bounds
        self.assertEqual(mango._get_edge(0, 0, 2), mango._get_edge(1, 0, 5))

        # test wrong value
        self.assertEqual(mango._get_edge(0, 0, 2), 'a')

        # test value outside bounds
        self.assertEqual(mango._get_edge(0, 0, 2), mango._get_edge(1, 1, 1))
