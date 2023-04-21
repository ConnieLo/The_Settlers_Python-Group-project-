class Road():
    """
    A road which exists on the board

    ATTRIBUTES

    owner: Player
        The Player to whom this road belongs

    position: tuple
        The position on the board at which this road exists, as an (x, y) tuple
    """

    def __init__(self, owner, position):
        print(position)
        self.owner = owner
        self.position = position