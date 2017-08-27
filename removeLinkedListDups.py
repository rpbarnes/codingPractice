"""
This goes through a linked list and removes the nodes that contain duplicate values from it.

"""
from singleLinkedListCycle import createLinkedList # theres just a function here that makes a linked list with or without a cycle in it

head = createLinkedList(listLen=30,makeCycle=False)

# def removeDuplicates(head):
dups = {}
node = head
while (node.next != head) and (node.next != None): # Just go through whole list
    found = dups.get(node.value)
    print found
    if found != None: # this node contains a duplicate
        node.previous.next = node.next
        node.next.previous = node.previous
    dups.update({node.value:1})
    node = node.next

node = head
print "New list"
while (node.next != head) and (node.next != None):
    print node.value
    node = node.next





