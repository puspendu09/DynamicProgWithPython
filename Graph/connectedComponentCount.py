count = 0
visited_node = ()


def connectedGraph(input_graph):
    for node in input_graph:
        print(node)
        return_value = hasPath(input_graph, node)
        if not return_value:
            global count
            count = count + 1


def hasPath(input_graph, src):
    # print(src)
    global visited_node
    if src in visited_node:
        return False
    visited_node = visited_node + tuple(src)
    for neighbour in input_graph:
        hasPath(input_graph, neighbour)

    return True


graph = {
    'a': ['b'],
    'b': ['a'],
    'c': []

}

connectedGraph(graph)
print(visited_node)
print(count)
