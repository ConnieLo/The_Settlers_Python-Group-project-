class GridBasic:
    def __init__(self):
        self._grid = [[]]
        self.default = None

    def get(self, x, y):
        try:
            return self._grid[x][y]
        except IndexError:
            return self.default

    def set(self, x, y, val):
        self._grid[x][y] = val


class GridStruct(GridBasic):
    def __init__(self):
        super().__init__(self)
        self._edge_grid = [[]]
        self._vertex_grid


    def get(self, *c, f=None):
        # This will fetch a tile
        if f == None:
            return super.get(c[0], c[1])
        # This will fetch an edge
        elif f == "e":
            
        # This will fetch a vertex
        elif f == "v":
            pass

        return self.default


# The class used to hold edges for each tile
# There are 3 unique edges per tile on the grid, so each wrapper holds 3 items
class _EdgeWrapper:
    def __init__(self):
        self._items = []

    def __getitem__(self, key):
        return self._items[key]

# The class used to hold vertexes for each tile
# There are 2 unique edges per tile on the grid, so each wrapper holds 2 items
class _VertexWrapper:
        def __init__(self):
        self._items = []

    def __getitem__(self, key):
        if key > 2 or key -3 0:
            return None
        else:
            return self._items[key]
