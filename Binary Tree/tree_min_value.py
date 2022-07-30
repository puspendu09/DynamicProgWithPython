from collections import deque
from math import inf


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#
# a = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')

a = Node(10)
b = Node(6)
c = Node(5)
d = Node(4)
e = Node(1)
f = Node(.5)

a.right = b
a.left = c
b.right = d
b.left = e
c.right = f


# depth first algo iterative

# def treeMinValue(root: Node):
#     tree_stack = [root]
#     smallest = inf
#     if root is None:
#         return smallest
#     while len(tree_stack) > 0:
#         current = tree_stack.pop()
#         current_value = current.val
#         if current_value < smallest:
#             smallest = current_value
#
#         if current.left is not None:
#             tree_stack.append(current.left)
#
#         if current.right is not None:
#             tree_stack.append(current.right)
#
#     return smallest


# breadth first algo iterative only possible

# def treeMinValue(root: Node):
#     tree_stack = deque([root])
#     smallest = inf
#     if root is None:
#         return smallest
#     while len(tree_stack) > 0:
#         current = tree_stack.popleft()
#         current_value = current.val
#         if current_value < smallest:
#             smallest = current_value
#
#         if current.left is not None:
#             tree_stack.append(current.left)
#
#         if current.right is not None:
#             tree_stack.append(current.right)
#
#     return smallest


print(treeMinValue(None))
