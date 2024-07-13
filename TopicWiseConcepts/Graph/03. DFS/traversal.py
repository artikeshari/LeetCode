class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val=val
        self.neighbors = neighbors if neighbors else []

def make_graph(egdes, num_node):
    graph = [Node(i+1) for i in range(num_node)]
    for e in egdes:
        graph[e[0]-1].neighbors.append(graph[e[1]-1])
        graph[e[1]-1].neighbors.append(graph[e[0]-1])

    for g in graph:
        print(f'{g.val} --> ', end='')
        for nn in g.neighbors:
            print(f'{nn.val}, ', end='')
        print("\n")        
    return graph

def DFS(node, visited):

    stack = [node]
    visited[node.val-1] = 1
    while stack:
        curr = stack[-1]
        stack.pop()
        print(curr.val)
        for nn in curr.neighbors:
            if not visited[nn.val-1]:
                visited[nn.val-1]=1
                stack.append(nn)

def main():
    edges = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    num_node = 5
    graph = make_graph(edges, num_node)
    visited = [0]*num_node
    DFS(graph[0], visited)

if __name__ == "__main__":
    main()