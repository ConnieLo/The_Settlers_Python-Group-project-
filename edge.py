import vertex
import centre

class Edge:
    
    def __init__(self):
        self.road = False
        self.owner = None

    def build_road(self, owner):
        self.owner = owner
        self.road = True