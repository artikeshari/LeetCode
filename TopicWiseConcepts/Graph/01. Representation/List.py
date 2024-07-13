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

def main():
    '''
    1 ------ 2
    |        |
    |        |
    3--------4
    '''
    input = [[1,2], [1,3], [3,4],[2,4]]
    make_graph(input,4)
        
if __name__ == "__main__":
    main()