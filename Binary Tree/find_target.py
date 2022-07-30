from collections import deque


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

a = Node(1)
b = Node(1)
c = Node(1)
d = Node(1)
e = Node(1)
f = Node(1)

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

#
# def find_target(root: Node, target):
#     queue = deque()
#     queue.append(root)
#     while len(queue) > 0:
#         current = queue.popleft()
#         if current is None:
#             return False
#         if current.val == target:
#             return True
#         if current.left is not None:
#             queue.append(current.left)
#         if current.right is not None:
#             queue.append(current.right)
#
#     return False


# def find_target(root: Node, target):
#     if root is None:
#         return False
#     if root.val == target:
#         return True
#
#     return find_target(root.left, target) or find_target(root.right, target)
#
#
# print(find_target(a, "e"))


# def tree_sum(root: Node):
#     if root is None:
#         return 0
#
#     return root.val + tree_sum(root.left) + tree_sum(root.right)

# def tree_sum(root: Node):
#     sum = 0
#     node_stack = [root]
#     if root is None:
#         return sum
#     while len(node_stack) > 0:
#         current = node_stack.pop()
#         sum = sum + current.val
#         if current.left is not None:
#             node_stack.append(current.left)
#         if current.right is not None:
#             node_stack.append(current.right)
#     return sum


def tree_sum(root: Node):
    sum = 0
    if root is None:
        return sum

    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        current = queue.popleft()
        sum = sum + current.val

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return sum


print(tree_sum(a))
