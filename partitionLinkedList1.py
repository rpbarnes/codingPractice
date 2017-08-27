"""
Build a linked list data structure then use the structure to make the manipulations you want to make.

You're almost there but there is still something wrong.

"""

class Node():
    def __init__(self, value): # defining by self allows for a circular list where the end points back to the beginning 
        self.value = value
        self.next = self
        self.previous = self

    def addBefore(self, other):
        self.previous.next = other
        other.previous = self.previous
        other.next = self
        self.previous = other

    def addAfter(self, other): 
        self.next.previous = other
        other.next = self.next
        self.next = other
        other.previous = self

    def insertBefore(self, other):
        other.previous.next = other.next # connect the previous and next nodes from where the other node came from.
        other.next.previous = other.previous
        self.previous.next = other # connect other to node before self
        other.previous = self.previous 
        other.next = self # connect other to self
        self.previous = other

class LinkedList():
    def __init__(self):
        self.Header = Node(None)
    
    def __nonzero__(self):
        return self.Header.next != self.Header

    def addNode(self, value):
        newNode = Node(value)
        self.Header.addBefore(newNode) # think about adding to the left of the header that points back around to the beginning.

    def printList(self):
        node = self.Header.next
        while node != self.Header and node.next != self.Header:
            print node.value
            node = node.next

    def partition(self, parVal):
        node = self.Header.next
        lastLess = False
        while node != self.Header and node.next != self.Header:
            nextNode = node.next
            if int(node.value) < int(parVal):
                if lastLess:
                    lastLess.insertBefore(node)
                else:
                    lastLess = node
            node = nextNode


# build list
l = LinkedList()
l.addNode(5)
l.addNode(1)
l.addNode(10)
l.addNode(4)
l.addNode(9)
l.addNode(2)
l.Header.addAfter(Node(4))
l.printList()

l.partition(5)
print "partitioned list"
l.printList()

