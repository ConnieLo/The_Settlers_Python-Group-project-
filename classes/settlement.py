from classes import player

class Settlement():

    def __init__(self, owner, potential_resources):
        self.owner: player = owner  #player instance
        self.is_city = False #boolean
        # Array of tuples (i, r) where i is a number and r is a string representation of a resource
        self.potential_resources = potential_resources


    # Takes an integer and check to see if it has any resources of that number it can give to the player
    def grant_resources(self, i):
        for num, res in self.potential_resources:
            if num == i:
                self.owner.add_resource(res)

