class GridBasic:
    def __init__(self):
        self._grid = [[None]]
        self.default = None

    def get(self, x, y):
        try:
            return self._grid[x][y]
        except IndexError:
            return self.default

    def set(self, x, y, val):
        self._touch(x, y)
        self._grid[x][y] = val

    # Returns true if a NONE NULL object exists at the given point, otherwise false
    def exists(self, x, y):
        try:
            return self._grid[x][y] != None
        except IndexError:
            return False
        
    # Checks to see if something exists at the given point, places a None object if not
    # Sorta like the unix command
    def _touch(self, x, y):
        # If the x axis isn't big enough - extend it
        if len(self._grid) <= x:
            self._grid.extend([[None] for n in range(x - len(self._grid) + 1)])

        # If the y axis isn't big enough, extend it
        if len(self._grid[x]) <= y:
            self._grid[x].extend([None for n in range(y - len(self._grid[x]) + 1)])


class GridStruct(GridBasic):
    def __init__(self):
        super().__init__()
        

    def get(self, *c, f=None):
        # This will fetch a tile
        tile = super().get(c[0], c[1])
        if f == None:
            return tile
        # This will fetch an edge
        elif f == "e":
            pass
        # This will fetch a vertex
        elif f == "v":
            pass

        return self.default
