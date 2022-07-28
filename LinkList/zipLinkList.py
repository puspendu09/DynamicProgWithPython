# creating linked list class
class Linkedlist:
    def __init__(self, values, next_node=None):
        self.values = values
        self.next_node = next_node


# creating nodes
nodeA = Linkedlist('a')
nodeB = Linkedlist('b')
nodeC = Linkedlist('c')
nodeM = Linkedlist('m')
nodeN = Linkedlist('n')
nodeO = Linkedlist('o')

# creating node list
nodeA.next_node = nodeB
nodeB.next_node = nodeC
nodeM.next_node = nodeN
nodeN.next_node = nodeO


# a->b->c
# m->n->o

def merge_link_list(head1, head2):
    tail = head1
    current1 = head1.next_node
    current2 = head2
    count = 0
    while current1 is not None or current2 is not None:
        if count % 2 == 0:
            tail.next_node = current2
            # count = count + 1
            current2 = current2.next_node
        else:
            tail.next_node = current1
            current1 = current1.next_node
            # count = count + 1

        count = count + 1

        tail = tail.next_node

    if current1 is not None:
        tail.next_node = current1

    if current2 is not None:
        tail.next_node = current2

    return head1


merge_link_list(nodeA, nodeM)


def print_list(node):
    while node is not None:
        print(node.values)
        node = node.next_node


print_list(nodeA)
