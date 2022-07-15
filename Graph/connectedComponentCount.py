def connectedComponentCount(graph, is_visited=None):
    count = 0
    if is_visited is None:
        is_visited = ()
        # count = 0
    for node in graph:
        # print(node)
        if explore(graph, node, is_visited) == True:
            count = count + 1
    return count


def explore(input_graph, current, is_visited):
    # print(current)
    if current in is_visited:
        # print(is_visited)
        return False
    is_visited = is_visited + tuple(current)
    print(is_visited)
    for neighbour in input_graph[current]:
        explore(input_graph, neighbour, is_visited)

        return True


graph = {
    'a': ['b'],
    'b': ['a'],
    'c': ['d'],
    'd': ['c'],
    # 6: [4, 5, 7, 8],
    # 7: [6],
    # 8: [6],
    # 9: [0]
}
# edges = [
#     ['i', 'j'],
#     ['k', 'i'],
#     ['m', 'k'],
#     ['k', 'l'],
#     ['o', 'n']
# ]

print(connectedComponentCount(graph))
