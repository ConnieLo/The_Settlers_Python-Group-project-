import settlement

class Vertex():

    def __init__(self, coords):
        self.coords = coords
        self.settlement = None

    def get_coords(self):
        return self.coords
    
    def add_settlement(self, owner): #incompletable till graph structure is complete
        self.settlement = settlement.Settlement(owner, [])#brackets will contain the 2/3 hexes the vertex connects to


        