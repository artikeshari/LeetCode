def make_graph(input):
    m = 0
    num_node = 4
    Graph = [[0]*num_node for i in range(num_node)]

    for e in input:
        Graph[e[0]-1][e[1]-1] = 1
        Graph[e[1]-1][e[0]-1] = 1

    for i in range(len(Graph)):
        print(f'{i+1}-->', end=' ')
        for j in range(len(Graph[i])):
            if Graph[i][j] == 1:
                print(j+1, end=',')
        print('\n')

def main():
    '''
    1 ------ 2
    |        |
    |        |
    3--------4
    '''
    input = [[1,2], [1,3], [3,4],[2,4]]
    make_graph(input)
        
if __name__ == "__main__":
    main()