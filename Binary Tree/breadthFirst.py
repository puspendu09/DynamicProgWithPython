class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.right = b
a.left = c
b.right = d
b.left = e
c.right = f

#    a
#  /   \
#  c    b
# /     / \
# f     e  d

from collections import deque

queue = deque()


def depth_first(node):
    value = []
    if node is None:
        return value
    queue.append(node)
    while len(queue) > 0:
        current = queue.popleft()
        value.append(current.val)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return value


print(depth_first(b))
