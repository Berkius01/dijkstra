import sys
 
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])
 
  
    def minDistance(self, dist, sptSet):
 
        # sonraki node için min değeri bulma
        min = sys.maxsize
 
        # shortest path içinde olmayan en yakın düğümü ara
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # gidilmemiş nodlara min uzaklığı bul 
            
            u = self.minDistance(dist, sptSet)
 
            # en küçük uzakığa sahip vertexi ekle
            sptSet[u] = True
 
           
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)
 
 

g = Graph(3)
g.graph = [[0, 4, 0, 0, 0, 0, 0],
           [0, 0, 8, 0, 0, 3, 0],
           [-1, 0, 0, 7, 0, 0, 0],
           [0, 0, 0, 0, 9, 0, 0],
           [1, 0, 0, 0, 0, 0, -3],
           [0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0 ]]
 
g.dijkstra(0)