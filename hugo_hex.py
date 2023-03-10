from math import sqrt


# Returns a 6-point coordinate list for a regular hexagon of a given sie around a given point
# param size:   The length of 1 regular side of the hexagon, equal to r_max
def hexagon(size, center):
    hu = size / 2  # Height unit
    wu = sqrt(size ** 2 - hu ** 2)  # Width unit
    return [
        (center[0], center[1] + 2 * hu),
        (center[0] + wu, center[1] + hu),
        (center[0] + wu, center[1] - hu),
        (center[0], center[1] - 2 * hu),
        (center[0] - wu, center[1] - hu),
        (center[0] - wu, center[1] + hu)
    ]


# A class to handel a 2d tessellating grid of regular hexagons, with co-ordinates pointing to each hex
class HexGrid:
    # Constructor
    # param size:   The length of 1 regular hexagon side
    # param center: The co-ordinates of the center of hex 0, 0
    def __init__(self, size,  center=[0, 0]):
        self.center = center
        self._r_min = (sqrt(3)/2) * size
        self._r_max = size
        self.hex_size = (int(2 * self._r_max), int(2 * self._r_max))

    # Returns the offset in pixel space of a given hex-coordinate, relative to the center of each hex tile
    def offset(self, x, y):
        x_offset = x * (2 * self._r_min) + self._r_min * y
        y_offset = y * (self._r_max * 1.5)

        return x_offset, y_offset

    # Returns the offset of the given hex co-ordinate, relative to the surface
    def absolute_offset(self, x, y):
        x_offset, y_offset = self.offset(x, y)
        return x_offset + self.center[0], y_offset + self.center[1]

    # Returns a tuple of 6 2d co-ordinates corresponding to the vertices of the hexagon
    def get_hex_vertices(self, x, y):
        x_offset, y_offset = self.offset(x, y)
        hex_center = [self.center[0] + x_offset, self.center[1] + y_offset]
        return hexagon(self._r_max, hex_center)


    # Returns the size of each hexagon's regular side
    def hex_size(self):
        return self._r_max