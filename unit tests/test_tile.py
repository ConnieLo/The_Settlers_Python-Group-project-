from unittest import TestCase

from classes.tile import Tile


class TestTile(TestCase):

    # Test if the class is initialized correctly with the provided values.
    def test_initialization(self):
        tile = Tile((0, 0), 'wood', 5)
        self.assertEqual(tile.coords, (0, 0))
        self.assertEqual(tile.resource, 'wood')
        self.assertEqual(tile.number, 5)

    # Test if the get_resource() method returns the correct resource value.
    def test_get_resource(self):
        tile = Tile((0, 0), 'brick', 8)
        self.assertEqual(tile.get_resource(), 'brick')

    # Test if the get_coords() method returns the correct coordinates.
    def test_get_coords(self):
        tile = Tile((1, 2), 'ore', 10)
        self.assertEqual(tile.get_coords(), (1, 2))

    # Test if the get_number() method returns the correct number.
    def test_get_number(self):
        tile = Tile((2, 1), 'wheat', 6)
        self.assertEqual(tile.get_number(), 6)

    # Test if the class can handle a negative number.
    def test_negative_number(self):
        tile = Tile((3, 3), 'sheep', -3)
        self.assertEqual(tile.get_number(), -3)

    # Test if the class can handle a float number.
    def test_float_number(self):
        tile = Tile((4, 4), 'wood', 5.5)
        self.assertEqual(tile.get_number(), 5.5)

    # Test if the class can handle a None value for the resource.
    def test_none_resource(self):
        tile = Tile((0, 1), None, 9)
        self.assertIsNone(tile.get_resource())

    # Test if the class can handle a None value for the coordinates.
    def test_none_coords(self):
        tile = Tile(None, 'brick', 3)
        self.assertIsNone(tile.get_coords())

    # if __name__ == '__main__':
    #     unittest.main()

    # def test_get_resource(self):
    #     self.fail()
    #
    # def test_get_coords(self):
    #     self.fail()
    #
    # def test_get_number(self):
    #     self.fail()
