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

def depth_first(node):
    node_stack = [node]

    # print(node)
    while len(node_stack) > 0:
        current = node_stack.pop()
        print(current.val)
        if current.right is not None:
            node_stack.append(current.right)
        if current.left is not None:
            node_stack.append(current.left)


depth_first(a)