count = 0
visit_node = ()
graph = {'a': [],
         'b': [],
         'c': [],
         'd': []}
# graph = {
#     'a': ['b', 'c'],
#     'b': ['d'],
#     'c': ['e'],
#     'd': ['f'],
#     'e': [],
#     'f': []
# }


def explore_graph(test_graph, start_node):
    global visit_node
    # to check if this node already visited
    if start_node in visit_node:
        return False
    # if not visited add this node to visited group
    else:
        visit_node = visit_node + tuple(start_node)
    # depth first traversal to check every connected node
    for neighbour in test_graph[start_node]:
        explore_graph(test_graph, neighbour)
    return True


for node in graph:
    if explore_graph(graph, node):
        count = count + 1

print(count)
