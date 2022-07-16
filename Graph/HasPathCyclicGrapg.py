def undirectedPath(input_edges, nodeA, nodeB, is_visited=None):
    graph = buildGraph(input_edges)
    if is_visited is None:
        is_visited = ()
    return hasPath(graph, nodeA, nodeB, is_visited)


def hasPath(inputGraph, src, tgt, is_visited):
    print(is_visited)
    if src == tgt:
        return True

    if src in is_visited:
        print("loop in this graph ", is_visited)
        return False
    is_visited = is_visited + tuple(src)

    for neighbour in inputGraph[src]:
        if hasPath(inputGraph, neighbour, tgt, is_visited):
            return True

    return False


# this method is used to build a graph from input edges
def buildGraph(input_edges):
    graph = {}
    for edge in input_edges:
        [a, b] = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(undirectedPath(edges, 'i', 'o'))
