# Returns the co-ordinates of the nth neighbor (clockwise) of the tile at the given co-ord
def neighbor_of(x, y, n):
    delta = [1, 1, 0, -1, -1, 0, 1]
    return x + delta[n], y + delta[n + 1]


class GridBasic:
    def __init__(self):
        self._grid = dict()

    def get(self, x, y, default=None):
        print(self._grid.keys())
        return self._grid.get((x, y), default)

    def set(self, x, y, val):
        self._grid[(x, y)] = val

    # Returns true if a NONE NULL object exists at the given point, otherwise false
    def exists(self, x, y):
        return (x, y) in self._grid.keys()


class GridStruct(GridBasic):
    def __init__(self):
        super().__init__()

    def get(self, *c, f=None):
        # Get the tile's held value
        if f is None:
            tile = super().get(c[0], c[1])

            # If tile is none, there's nothing there
            if tile is None:
                return None

            return tile.val
        # Get a vertex
        elif f == "v":
            return self._get_vertex(*c)
        # Get an edge
        elif f == "e":
            pass

    # This is really gross I don't like it...
    # because of how Python handles unpacking args with * I just have to TRUST that c[2] is val
    def set(self, *c, f=None):
        # Setting a tile
        if f is None:
            pass
        # Setting a vertex
        elif f == "v":
            pass
        # setting a vertex
        elif f == "e":
            pass

    def _get_vertex(self, x, y, z):
        # This function uses recursive logic, the base case being when z is either 0 or 1

        # VERTICES
        # z = 2 -> v 0 of neighbor 2
        # z = 3 -> v 1 of neighbor 3
        # z = 4 -> v 0 of neighbor 3
        # z = 5 -> v 1 of neighbor 4
        if z == 0 or z == 1:
            tile = super().get(x, y)

            # If tile is none, there's nothing there
            if tile is None:
                return None

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
        # VERTICES
        # z = 2 -> v 0 of neighbor 2
        # z = 3 -> v 1 of neighbor 3
        # z = 4 -> v 0 of neighbor 3
        # z = 5 -> v 1 of neighbor 4
        if z == 0 or z == 1:
            # Get the tile wrapper, or create a new one
            if not super().exists(x, y):
                super().set(x, y, _TileWrapper())
            tile = super().get(x, y)

            tile.v[z] = val
        elif z == 2:
            self._set_vertex(*neighbor_of(x, y, 2), 0, val)
        elif z == 3:
            self._set_vertex(*neighbor_of(x, y, 3), 1, val)
        elif z == 4:
            self._set_vertex(*neighbor_of(x, y, 3), 0, val)
        elif z == 5:
            self._set_vertex(*neighbor_of(x, y, 4), 1, val)


class _TileWrapper:
    def __init__(self, val=None):
        self.val = val
        self.v = [None] * 2
        self.e = [None] * 3
