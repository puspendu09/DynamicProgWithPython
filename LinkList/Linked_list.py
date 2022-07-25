# creating linked list class
class Linkedlist:
    def __init__(self, values, next_node=None):
        self.values = values
        self.next_node = next_node


# creating nodes
nodeA = Linkedlist('a')
nodeB = Linkedlist('b')
nodeC = Linkedlist('c')

# creating node list
nodeA.next_node = nodeB
nodeB.next_node = nodeC


# reverse a linkedlist

def reverse_list(head: Linkedlist):
    current = head
    previous = None
    while current is not None:
        # print(current.values)
        next = current.next_node
        current.next_node = previous
        previous = current
        current = next


# access a linkedlist
def print_list(node: Linkedlist):
    while node is not None:
        print(node.values)
        node = node.next_node


# original linked list
print_list(nodeA)
# invoking reverse method
reverse_list(nodeA)
# after reversal
print_list(nodeC)
