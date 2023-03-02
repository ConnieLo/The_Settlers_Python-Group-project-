import vertex
import centre

class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.player = None
        self.road = False


#class Edge:
    
#    def __init__(self):
#        self.road = False
#        self.owner = None

#    def build_road(self, owner):
#        self.owner = owner
#        self.road = True