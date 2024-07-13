#!/usr/bin/python
from collections import deque

class Node(object):
    def __init__(self, val=0, neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors else []    


def make_graph(input, num_node):
    Graph = [Node(i+1) for i in range(num_node)]

    for e in input:
        Graph[e[0]-1].neighbors.append(Graph[e[1]-1])
        Graph[e[1]-1].neighbors.append(Graph[e[0]-1])

    for node in Graph:
        print(f'{node.val}-->', end=' ')
        for nn in node.neighbors:
            print(nn.val, end=',')
        print('\n')

    return Graph

def BFS(node, visited):
    print("----- Printing BFS -----")
    que = deque()
    que.append(node)
    visited[node.val-1] = 1
    while que:
        curr = que[0]
        print(curr.val)
        que.popleft()
        for nn in curr.neighbors:
            if not visited[nn.val-1]:
                visited[nn.val-1]=1
                que.append(nn)                    
    pass

def main():
    '''
    1 ------ 2
    |        |
    |        |
    3--------4
    '''
    input = [[1,2], [1,3], [3,4],[2,4]]
    num_node = 4
    graph = make_graph(input, num_node)
    visited = [0]*num_node

    BFS(graph[1], visited)

        
if __name__ == "__main__":
    main()