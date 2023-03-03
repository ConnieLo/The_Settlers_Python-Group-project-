# Returns the co-ordinates of the nth neighbor (clockwise) of the tile at the given co-ord
def neighbor_of(x, y, n):
    delta = [1, 1, 0, -1, -1, 0, 1]
    return x + delta[n], y + delta[n + 1]


class GridBasic:
    def __init__(self):
        self._grid = dict()
        self.default = None

    def get(self, x, y):
        print(self._grid.keys())
        return self._grid.get((x, y), None)

    def set(self, x, y, val):
        self._grid[(x, y)] = val

    # Returns true if a NONE NULL object exists at the given point, otherwise false
    def exists(self, x, y):
        return (x, y) in self._grid.keys()


class GridStruct(GridBasic):
    def __init__(self):
        super().__init__()

    def get(self, *c, f=None):
        # This will fetch a _TileWrapper object
        tile = super().get(c[0], c[1])

        if tile is None:
            return None

        return tile.val

    # This is really gross I don't like it...
    # because of how Python handles unpacking args with * I just have to TRUST that c[2] is val
    def set(self, *c, f=None):
        if len(c) < 3:
            raise Exception("No value passed to GridStruct.set()")
        new_tile = _TileWrapper(c[2])
        super().set(c[0], c[1], new_tile)


class _TileWrapper:
    def __init__(self, val):
        self.val = val
