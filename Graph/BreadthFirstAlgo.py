from collections import deque

queue = deque()
graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def breadth_first(input_graph, source):
    queue.append(source)
    while len(queue) > 0:
        current = queue.popleft()
        print(current)
        for neighbour in input_graph[current]:
            queue.append(neighbour)


breadth_first(graph, 'a')
