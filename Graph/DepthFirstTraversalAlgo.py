graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


# iterative method for depth first
# def depth_first(input_graph, source):
#     stack = [source]
#     while len(stack) > 0:
#         current = stack.pop()
#         print(current)
#         for neighbour in input_graph[current]:
#             stack.append(neighbour)

# recursive method for depth first
def depth_first(input_graph, source):
    print(source)
    for neighbour in input_graph[source]:
        depth_first(input_graph, neighbour)


depth_first(graph,'a')
