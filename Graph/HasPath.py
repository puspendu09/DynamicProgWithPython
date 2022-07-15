from collections import deque

# depth first approach fo find the path if exist
# def has_path(input_graph, src, tgt):
#     if src == tgt:
#         return True
#
#     for neighbour in graph[src]:
#         if has_path(input_graph, neighbour, tgt):
#             return True
#
#     return False


# breadth first approach
queue = deque()


def has_path(input_graph, src, tgt):
    # if src == tgt:
    #     return True
    queue.append(src)
    while len(queue) > 0:
        current = queue.popleft()
        if current == tgt:
            return True
        for neighbour in input_graph[current]:
            queue.append(neighbour)

    else:
        return False


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

print(has_path(graph, 'b', 'd'))
