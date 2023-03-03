import settlement

class Vertex():

    def __init__(self, coords):
        self.coords = coords
        self.settlement = None

    def get_coords(self):
        return self.coords
    
    def add_settlement(self, player): #incompletable till graph structure is complete
        self.settlement = settlement.Settlement(player, [])#brackets will contain the 2/3 hexes the vertex connects to
