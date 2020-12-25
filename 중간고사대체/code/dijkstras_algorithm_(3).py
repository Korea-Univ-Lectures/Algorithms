import copy

INF  = 999999

class Graph(): 
  
        def __init__(self, vertices): 
                self.V = vertices 
                self.graph = [[0 for column in range(vertices)]  
                        for row in range(vertices)]
        def set_graph(self, edges):
                for i in range(self.V):
                        for j in range(self.V):
                                if edges[i][j] == INF:
                                        self.graph[i][j] = 999999
                                else:
                                        self.graph[i][j] = int(edges[i][j])
        
        def printSolution(self, dist): 
                print ("Vertex \tDistance from Source")
                for node in range(self.V): 
                        if dist[node] != 999999:
                                print(str(node)+"\t"+str(dist[node]))
                        else:
                                print(str(node)+"\tINF")

        def minDistance(self, dist, sptSet): 

                min = 999999
                
                for v in range(self.V):
                        
                        if dist[v] < min and sptSet[v] == False: 
                                min = dist[v] 
                                min_index = v
                print(dist)
                print(sptSet)
                print(min_index)
                return min_index 
        
        def dijkstra(self, src):
                '''
                for i in range(src):
                        for j in range(src):
                                self.graph[i].append(self.graph[i][0])
                                self.graph[i].pop(0)

                for i in range(src):
                        self.graph.append(self.graph[0])
                        self.graph.pop(0)'''
                S = set()
                S.add(src)
                V = set()
                for v in range(self.V):
                        V.add(v)

                dist = copy.deepcopy(self.graph[src])
                #print(dist)

                for i in range(0, self.V):
                        min_dist_dict = dict()
                        if len((V-S)) > 0:
                                for vertex in list(V-S):
                                        min_dist_dict[vertex] = dist[vertex]
                                #print(min_dist_dict)

                                value_list = list(min_dist_dict.values())
                                #print(type(value_list))
        
                                w_index = value_list.index(min(value_list))
                                key_list = list(min_dist_dict.keys())
                                w = key_list[w_index]
                                #print(w)
                                S.add(w)
                                #print(w)
                                for j in list(V-S):
                                        dist[j] = min(dist[j], dist[w] + self.graph[w][j])

        
                self.printSolution(dist) 

g = Graph(3)

graph = [[0, 5, 12], 
        [INF, 0, 3], 
        [8, INF, 0]] 
g.set_graph(graph)
g.dijkstra(1)


g = Graph(4)
graph = [[0, 5, INF, 10], 
        [INF, 0, 3, INF], 
        [INF, INF, 0, 1], 
        [INF, INF, INF, 0]] 
g.set_graph(graph)
g.dijkstra(2)
  
g = Graph(5)

graph = [[0, 9, 34, 10, INF], 
        [INF, 0, 27, 7, 34], 
        [17, 100, 0, 1, INF], 
        [12, 1, INF, 0, 5],
        [4, INF, INF, 3, 0]] 
g.set_graph(graph)
g.dijkstra(4)