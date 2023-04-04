import random as rnd
import itertools as itt

class Board:
    def __init__(self):
        self.tiles = self.generate_tiles()
        self.foo = "bar"

    def generate_tiles(self):
        new_tiles = []

        # The resource pool
        resources = []
        resources.extend(["sheep"] for i in range(4))
        resources.extend(["wheat"] for i in range(4))
        resources.extend(["wood"] for i in range(4))
        resources.extend(["ore"] for i in range(4))
        resources.extend(["clay"] for i in range(4))
        rnd.shuffle(resources)

        # The number tokens pool
        # There whould be two of every number between 2 and 12
        # but NO 7s, only ONE 2, and only ONE 12
        numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        rnd.shuffle(numbers)

        # Assigning the numbers and resources randomly
        for i in range(18):
            new_tiles.append((numbers[i], resources[i]))

        # Putting the desert at a random spot
        new_tiles.insert(rnd.randint(0, 18), (0, "desert"))

        return new_tiles


b = Board()
print(b.tiles)