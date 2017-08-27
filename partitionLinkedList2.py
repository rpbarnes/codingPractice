class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(node):
    while node:
        print node.val,
        node = node.next
    print    

def Partition(head, x):
    x_node = Node(x)
    x_node.next = head
    current = head
    last = x_node
    while current:
        if current.val < x_node.val:
            last = last.next
            temp_val = current.val
            current.val = last.val
            last.val = temp_val
        current = current.next
    temp_val = last.val
    last.val = x_node.val
    x_node.val = temp_val
       
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(12)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(100)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10


Partition(node1, 5)
print_list(node1)
