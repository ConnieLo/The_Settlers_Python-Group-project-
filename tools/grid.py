# An array to translate between indexing and co-ordinates (ie a[0] being the bottom left most
# tile, at co-ordinate -2,-2
CONSTANT_COORDS = (
    (-2, -2),
    (-1, -2),
    (0, -2),
    (-2, -1),
    (-1, -1),
    (0, -1),
    (1, -1),
    (-2, 0),
    (-1,0),
    (0, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (2, 1),
    (0, 2),
    (1, 2),
    (2, 2)
)


# Translates between co-ords and indexes
def coord_to_index(i):
    return CONSTANT_COORDS.index(tuple(i))


# Translates between co-ords and indexes
def index_to_coord(i):
    return CONSTANT_COORDS[i]


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

    # returns the tile at (x, y) or creates a new, empty one if there is nothing there
    def _touch(self, x, y):
        if not super().exists(x, y):
            tile = _TileWrapper()
            super().set(x, y, tile)
        else:
            tile = super().get(x, y)
        return tile

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
        if z <= 1:
            # Get the tile wrapper, or create a new one
            tile = self._touch(z, y)
            tile.v[z] = val
        elif z == 2:
            self._set_vertex(*neighbor_of(x, y, 2), 0, val)
        elif z == 3:
            self._set_vertex(*neighbor_of(x, y, 3), 1, val)
        elif z == 4:
            self._set_vertex(*neighbor_of(x, y, 3), 0, val)
        elif z == 5:
            self._set_vertex(*neighbor_of(x, y, 4), 1, val)

    def _get_edge(self, x, y, z):
        # EDGES
        # z = 3 -> e0 of n3
        # z = 4 -> e1 of n4
        # z = 5 -> e2 of n5
        if z <= 2:
            tile = super().get(x, y)

            # If tile is none, there's nothing there
            if tile is None:
                return None

            return tile.e[z]
        elif z <= 5:
            return self._get_edge(*neighbor_of(x, y, z), z-3)

    def _set_edge(self, x, y, z, val):
        # EDGES
        # z = 3 -> e0 of n3
        # z = 4 -> e1 of n4
        # z = 5 -> e2 of n5
        # Which means we can do it in one if/else statement BABYYYY
        if z <= 2:
            tile = self._touch(x, y)
            tile.e[z] = val
        elif z <= 5:
            self._set_edge(*neighbor_of(x, y, z), z-3)


class _TileWrapper:
    def __init__(self, val=None):
        self.val = val
        self.v = [None] * 2
        self.e = [None] * 3
