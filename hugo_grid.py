class Grid:
    def __init__(self):
        self._grid = [[]]
        self.default = None

    def get(self, x, y):
        try:
            return self._grid[x][y]
        except IndexError:
            return self._default

    def set(self, x, y, val):
        self._grid[x][y] = val