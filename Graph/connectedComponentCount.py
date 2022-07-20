count = 0
visit_node = ()
# graph = {'a': ['b'],
#          'b': ['a'],
#          'c': [],
#          'd': []}
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def explore_graph(test_graph, start_node):
    global visit_node
    if start_node in visit_node:
        return False
    else:
        visit_node = visit_node + tuple(start_node)

    for neighbour in test_graph[start_node]:
        explore_graph(test_graph, neighbour)
    return True


for node in graph:
    if explore_graph(graph, node):
        count = count + 1

print(count)
