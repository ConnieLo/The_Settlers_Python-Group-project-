from classes import player

class Settlement():

    def __init__(self, owner, settlement_info):
        self.owner: player.Player = owner  #player instance
        self.is_city = False #boolean
        # Array of tuples (i, r) where i is a number and r is a string representation of a resource
        self.settlement_info = settlement_info


    # Takes an integer and check to see if it has any resources of that number it can give to the player
    def grant_resources(self, i):
        for res, num, *_ in self.settlement_info:
            if num == i:
                self.owner.add_resource(res)

