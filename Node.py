class Node():

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.neighbours = []

    def edge(self, node):
        self.neighbours.append(node)

    def __str__(self):
        return f'({self.vertex_number})'

    def outDegree(self):
        return len(self.neighbours)

def printGraph(nodes):
    for n in nodes:
        for neighbour in n.neighbours:
            print(f'{n} -> {neighbour}')
            #sau print(str(n) + ' -> ' + str(neighbour))

def highestOutDegree(nodes):
    node = None
    dictionar = {n.outDegree(): n.vertex_number for n in nodes}
    node = max([k for k in dictionar.keys()])
    return dictionar[node]

def createRandomSubgraph(nodes):
    import random
    subgraph = []
    nr_vertices = int(0.6 * len(nodes))
    nodes_chosen = random.choices(nodes, k=nr_vertices)
    for node in nodes_chosen:
        nr_edges = int(0.8 * len(node.neighbours))
        vecini_alesi = random.choices(node.neighbours, k=nr_edges)
        node.neighbours = vecini_alesi
        subgraph.append(node)
nodes = []

for i in range(7):
    nodes.append(Node(i))
nodes[1].edge(nodes[3])
nodes[1].edge(nodes[6])
nodes[2].edge(nodes[6])
nodes[3].edge(nodes[3])
nodes[3].edge(nodes[4])
nodes[5].edge(nodes[2])
nodes[6].edge(nodes[3])
nodes[6].edge(nodes[4])
nodes[6].edge(nodes[5])