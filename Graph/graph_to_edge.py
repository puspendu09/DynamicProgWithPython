test_graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e', 'a'],
    'd': ['f'],
    'e': [],
    'f': []
}


def graph_to_edge(graph):
    edges = []
    for node in graph:
        a = node
        for neighbour in graph[node]:
            b = neighbour
            edge = [a, b]
            edges.append(edge)

    return edges


print(graph_to_edge(test_graph))
