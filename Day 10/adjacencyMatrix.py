#------------------------ ADJACENCY MATRIX ----------------------------------#

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0 for _ in range(vertices)]
                       for _ in range(vertices)]
        
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[u][v] = 1
        
    def dispaly(self):
        for row in self.matrix:
            print(row)

g = Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,0)
g.add_edge(1,3)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(3,2)

print("Adjacency matrix : ")
g.dispaly()
