# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:09:13 2021

@author: Tony Zhou
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:46:56 2021

@author: Tony Zhou
"""

from collections import defaultdict

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
        
def takeInput():
    fl = input()
    fl = fl.split(' ')
    num_nuts = int(fl[0])
    num_bolts = int(fl[1])
    bolt_status = []
    for i in range(num_nuts):
        temp = input()
        temp = temp.split(' ')
        bolt_status.append(split(temp))
    
    return bolt_status,num_nuts,num_bolts

def redraw_Graph(bst,nn,nb):
    length = nn + nb + 2
    graph = []
    # add source and sink to the graph info
    source = []
    sink = [] 
    # firstly build source and sink node
    
    for i in range(length):
        source.append(0)
        sink.append(0)
    for i in range(nn+1):
        if i == 0:
            continue
        else:
            source[i] = 1
    graph.append(source)
    # Then construct the part where nut nodes are directed to bolt nodes
    middleBlock = []
    for i in range(nn):
        tempNode = []
        for j in range(length):
            if j <= nn:
                tempNode.append(0)
            elif j == length-1:
                tempNode.append(0)
            else:
                col=j-(nn+1)
                tempNode.append(int(bst[i][j-(nn+1)]))
        graph.append(tempNode)
        middleBlock.append(tempNode)
    # Then construct the slots node that direct to the sink
    endBlock = []
    for i in range(nb):
        tempNode = []
        for j in range(length):
            if j == length-1:
                tempNode.append(1)
            else:
                tempNode.append(0)
        graph.append(tempNode)
        endBlock.append(tempNode)
    
    # Finally build up the graph with source, middlepart
    graph.append(sink)
    return graph
    
    
    
    

def split(word):
    return [char for char in word]   

def driver():
    bst,nn,nb = takeInput()
    s = 0
    t = nn+nb+1
    g = redraw_Graph(bst, nn, nb)
    graph = Graph(g)
    

    print(graph.ford_fulkerson(s,t))

  
    
    
if __name__ == "__main__":
    driver()
    