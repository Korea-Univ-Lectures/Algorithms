INF  = 9999999999999

class Graph:
    def __init__(self, vertices): 
        self.V = vertices 

    def floyd(self, graph): 
        reach =[i[:] for i in graph] 
        for k in range(self.V): 
            for i in range(self.V): 
                for j in range(self.V):
                    reach[i][j] = min(reach[i][j], reach[i][k]+reach[k][j]) 
        self.printSolution(reach) 
    
    def printSolution(self, dist): 
        print ("shortest distances of the given graph")     
        for i in range(self.V):
            solution_string = []
            for j in range(self.V):
                if(dist[i][j] == INF):
                    solution_string.append("INF")
                else:
                    solution_string.append(str(dist[i][j]))
            print(solution_string)

g = Graph(3)

graph = [[0, 5, 12], 
        [INF, 0, 3], 
        [8, INF, 0]
        ] 

g.floyd(graph)


g = Graph(4)

graph = [[0, 5, INF, 10], 
        [INF, 0, 3, INF], 
        [INF, INF, 0, 1], 
        [INF, INF, INF, 0] 
        ] 

g.floyd(graph)

g = Graph(5)

graph = [[0, 9, 34, 10, INF], 
        [INF, 0, 27, 7, 34], 
        [17, 100, 0, 1, INF], 
        [12, 1, INF, 0, 5],
        [4, INF, INF, 3, 0], 
        ] 

g.floyd(graph)