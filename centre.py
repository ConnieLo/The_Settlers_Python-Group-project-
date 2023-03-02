import vertex

class Tile: #could be renamed to tile?
    
    def __init__(self, resource, number):
        self.resource = resource
        self.number = number

    def __str__(self):
        return f"Tile {self.number}: {self.resource_type}"

