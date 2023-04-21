from classes import player

class Settlement():
    """
    Represents a single settlement OR city

    ATTRIBUTES

    owner: Player
        The player to whom this settlement belongs

    is_city: Bool
        True if the settlement is a city

    settlement_info: List
        A representation of the tiles adjacent to this city. Stored as an array of tuples
        (i, r) where i is a number and r is a string representation of a resource
    """
    def __init__(self, owner, settlement_info):
        self.owner: player.Player = owner
        self.is_city = False
        self.settlement_info = settlement_info

    def grant_resources(self, i):
        """
        Takes a dice roll and check to see if it has any resources of that number it can give to the player - which
        it then grants
        :param i: int
            The dice roll
        """
        print(self.settlement_info)
        for (num, res) in self.settlement_info:
            if num == i:
                self.owner.add_resource(res)