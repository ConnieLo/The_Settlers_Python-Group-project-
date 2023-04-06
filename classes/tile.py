class Tile:

    def __init__(self, coords, resource, number):
        self.coords = coords
        self.resource = resource
        self.number = number

    
    #unsure if these getters are needed; can get rid of them in future
    def get_resource(self):
        return self.resource
    
    def get_coords(self):
        return self.coords
    
    def get_number(self):
        return