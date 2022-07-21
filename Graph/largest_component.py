visited_node = ()

graph = {
    'a': ['b', 'e', 'g'],
    'b': ['a'],
    'e': ['a'],
    'g': ['a'],
    'c': ['d', 'f'],
    'f': ['d', 'c'],
    'd': ['f', 'c']
}


def largest_component(graph):
    largest = 0
    for node in graph:
        size = explore(node, graph)
        if size > largest:
            largest = size
    return largest


def explore(node, graph):
    global visited_node
    if node in visited_node:
        return 0
    else:
        visited_node = visited_node + tuple(node)

    size = 1
    for neighbour in graph[node]:
        size = size + explore(neighbour, graph)

    return size


print(largest_component(graph))
