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
        # If tile is none, there's nothing there
        # Note this is NOT the same as having a tile with no data, as it may still point to edges and vertices
        # which DO have data
        if tile is None:
            return None

        # Get the tile's held value
        if f is None:
            return tile.val
        # Get a vertex
        elif f == "v":
            pass
        # Get an edge
        elif f == "e":
            pass

    # This is really gross I don't like it...
    # because of how Python handles unpacking args with * I just have to TRUST that c[2] is val
    def set(self, *c, f=None):
        if len(c) < 3:
            raise Exception("No value passed to GridStruct.set()")
        new_tile = _TileWrapper(c[2])
        super().set(c[0], c[1], new_tile)

    def _get_vertex(self, x, y, z):
        # VERTICES
        # z = 2 -> v 0 of neighbor 2
        # z = 3 -> v 1 of neighbor 3
        # z = 4 -> v 0 of neighbor 3
        # z = 5 -> v 1 of neighbor 4
        if z == 0 or z == 1:
            tile = super().get(x, y)
            return tile.v[z]
        elif z == 2:
            return self._get_vertex(*neighbor_of(x, y, 2), 0)
        elif z == 3:
            return self._get_vertex(*neighbor_of(x, y, 3), 1)
        elif z == 4:
            return self._get_vertex(*neighbor_of(x, y, 3), 0)
        elif z == 5:
            return self._get_vertex(*neighbor_of(x, y, 4), 1)

    def _set_vertex(self, x, y, z, val):
        if z == 0 or z == 1:
            tile = super().get(x, y)
            tile.v[z] = val
        elif z == 2:
            return self._set_vertex(*neighbor_of(x, y, 2), 0, val)
        elif z == 3:
            return self._set_vertex(*neighbor_of(x, y, 3), 1, val)
        elif z == 4:
            return self._set_vertex(*neighbor_of(x, y, 3), 0, val)
        elif z == 5:
            return self._set_vertex(*neighbor_of(x, y, 4), 1, val)


class _TileWrapper:
    def __init__(self, val=None):
        self.val = val
        self.v = [None] * 2
        self.e = [None] * 3
