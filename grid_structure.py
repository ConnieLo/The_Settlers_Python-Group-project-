# Returns the co-ordinates of the nth neighbor (clockwise) of the tile at the given co-ord
def neighbor_of(x, y, n):
    delta = [1, 1, 0, -1, -1, 0, 1]
    return x + delta[n], y + delta[n + 1]


class GridBasic:
    def __init__(self):
        self._grid = [[None]]
        self.default = None

    def get(self, x, y):
        try:
            return self._grid[x][y]
        except IndexError:
            return self.default

    def set(self, x, y, val):
        self._touch(x, y)
        self._grid[x][y] = val

    # Returns true if a NONE NULL object exists at the given point, otherwise false
    def exists(self, x, y):
        try:
            return self._grid[x][y] != None
        except IndexError:
            return False
        
    # Checks to see if something exists at the given point, places a None object if not
    # Sorta like the unix command
    def _touch(self, x, y):
        # If the x axis isn't big enough - extend it
        if len(self._grid) <= x:
            self._grid.extend([[None] for n in range(x - len(self._grid) + 1)])

        # If the y axis isn't big enough, extend it
        if len(self._grid[x]) <= y:
            self._grid[x].extend([None for n in range(y - len(self._grid[x]) + 1)])


class GridStruct(GridBasic):
    def __init__(self):
        super().__init__()
        

    def get(self, *c, f=None):
        # This will fetch a tile
        tile = super().get(c[0], c[1])
        if f == None:
            return tile
        # This will fetch an edge
        elif f == "e":
            pass
        # This will fetch a vertex
        elif f == "v":
            pass

        return self.default


    #### FIN'S GRAPH ####
class Graph:
    def __init__(self, name):
        self.name = name
        self.vertices = {}  # dictionary to store the vertices in the graph
        self.edges = set()  # set to store the edges in the graph

    def __repr__(self):
        return f"Graph({self.name})"

    def add_vertex(self, key):
        vertex = Vertex(key)  # create a new Vertex object with the given key
        self.vertices[key] = vertex  # add the vertex to the dictionary

    def add_edge(self, key1, key2):
        if key1 not in self.vertices:
            self.add_vertex(key1)  # add vertex1 to the graph if it doesn't exist
        if key2 not in self.vertices:
            self.add_vertex(key2)  # add vertex2 to the graph if it doesn't exist
        vertex1 = self.vertices[key1]  # get the Vertex object for vertex1
        vertex2 = self.vertices[key2]  # get the Vertex object for vertex2
        if vertex1 != vertex2:  # check that the edge doesn't already exist
            edge = Edge(vertex1, vertex2)  # create an Edge object for the new edge
            self.edges.add(edge)  # add the edge to the set of edges

    def get_vertices(self):
        return self.vertices.keys()  # return a list of the keys for all vertices in the graph

    def get_edges(self):
        return self.edges  # return the set of all edges in the graph

    def get_edge(self, key1, key2):
        vertex1 = self.vertices.get(key1)
        vertex2 = self.vertices.get(key2)
        if vertex1 is None or vertex2 is None:
            return None  # return None if either vertex doesn't exist
        for edge in self.edges:
            if (edge.vertex1 == vertex1 and edge.vertex2 == vertex2) or (
                    edge.vertex1 == vertex2 and edge.vertex2 == vertex1):
                return edge.vertex1.key, edge.vertex2.key  # return the edge between the two vertices if it exists
        return None  # return None if no edge exists between the two vertices

    def get_edges_for_vertex(self, key):
        vertex = self.vertices.get(key)  # get the Vertex object for the given key
        if vertex is None:
            return None  # return None if the vertex doesn't exist
        edges_for_vertex = set()
        for edge in self.edges:
            if vertex in (edge.vertex1, edge.vertex2):
                edges_for_vertex.add((edge.vertex1.key, edge.vertex2.key))
        return edges_for_vertex     # returns all the edges connected to the given vertex


class Vertex:
    def __init__(self, key):
        self.key = key  # unique identifier for the vertex
        self.neighbours = set()  # set to store the vertex's neighbors

    def add_neighbor(self, neighbour):
        self.neighbours.add(neighbour)  # add a neighboring vertex to the set

    def get_neighbours(self):
        return self.neighbours  # return the set of neighbors for the vertex


class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1  # one endpoint of the edge
        self.vertex2 = vertex2  # the other endpoint of the edge