from math import sqrt


def hexagon(size, center):
    """
    Returns a 6-point coordinate list for a regular hexagon of a given size around a given point

    :param size:
        The length of 1 regular side of the hexagon, equal to r_max
    :param center:
        The co-ordinate around which the hexagon is to be centered
    :return:
        A list of 6 co-ordinates, starting from the vertex at '12o.clock', going clockwise
    """
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


class HexGrid:
    """
    A class to handel a 2d tessellating grid of regular hexagons, with co-ordinates pointing to each hex

    ATTRIBUTES

    center:
        The co-ordinate at the center of tile 0, 0
    _r_min:
        distance from center to the midpoint of any given edge
    _r_max:
        distance from center to any given vertex
    hex_size:
        The dimensions of a square which would enclose a single hexagon - useful for rendering images

    (NOTE: _r_min and _r_max are dependent on each other, and one could be derived from the other. In theory only one
    is needed, however having both stored makes code quicker and more readable. They are meant to be PRIVATE, hence the
    leading underscore according to pythonic convention. GREAT CARE should be taken before changing them, as
    changing one will not automatically update the other, and the ration must be kept the same.)
    """

    def __init__(self, size,  center=[0, 0]):
        """
        Constructor
        :param size:
            The length of 1 regular hexagon side
        :param center:
            The co-ordinates of the center of hex 0, 0
        """
        self.center = center
        self._r_min = (sqrt(3)/2) * size
        self._r_max = size
        self.hex_size = (int(2 * self._r_max), int(2 * self._r_max))

    def offset(self, x, y):
        """
        Calculates the offset in pixel space of a given hex-coordinate, relative to the center of each hex tile
        :param x:
            The x co-ordinate
            this is a HEX GRID co-ordinate, not an absolute one
        :param y:
            The y co-ordinate
            this is a HEX GRID co-ordinate, not an absolute one
        :return:
            The relative offset in pixels between the given point and the hexagon 0, 0.
        """
        x_offset = x * (2 * self._r_min) + self._r_min * y
        y_offset = y * (self._r_max * 1.5)

        return x_offset, y_offset

    def absolute_offset(self, x, y):
        """
        Returns the offset of the given hex co-ordinate, relative to the surface
        :param x:
            The x co-ordinate
            this is a HEX GRID co-ordinate, not an absolute one
        :param y:
            The y co-ordinate
            this is a HEX GRID co-ordinate, not an absolute one
        :return:
        The offset in pixels between the given point and the origin point of the display
        """
        x_offset, y_offset = self.offset(x, y)
        return x_offset + self.center[0], y_offset + self.center[1]

    def get_hex_vertices(self, x, y):
        """
        Returns a tuple of 6 2d co-ordinates corresponding to the vertices of the hexagon
        :param x:
            The x co-ordinate
            this is a HEX GRID co-ordinate, not an absolute one
        :param y:
            The y co-ordinate
            this is a HEX GRID co-ordinate, not an absolute one
        :return:
            A list of 6 co-ordinates, starting from the vertex at '12o.clock', going clockwise
        """
        x_offset, y_offset = self.offset(x, y)
        hex_center = [self.center[0] + x_offset, self.center[1] + y_offset]
        return hexagon(self._r_max, hex_center)

    def hex_size(self):
        """
        Accessor for _r_max
        :return:
            the size of each hexagon's regular side
        """
        return self._r_max