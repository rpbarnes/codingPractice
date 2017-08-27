"""
This partions the list about a value given by the user


"""

from singleLinkedListCycle import createLinkedList # theres just a function here that makes a linked list with or without a cycle in it

head = createLinkedList(listLen=10,makeCycle=False)
partition = 50

def insertNode(node,lastLess,lastGreater):
    node.previous = lastLess
    node.next = lastGreater
    if lastLess != None:
        lastLess.next = node
    if lastGreater != None:
        lastGreater.previous = node
    return lastLess,lastGreater

#def partition(head,partition):
node = head
lastLess = None
lastGreater = None
countL = 0
countG = 0
while (node.next != head) and (node.next != None):
    nextNode = node.next
    # insert the node between the lastLess and lastGreater
    if lastLess != None:
        lastLess.next = node
        node.previous = lastLess
    if lastGreater != None:
        lastGreater.previous = node
        node.next = lastGreater
    if node.value < partition:
        if countL == 0:
            headNew = node
            headNew.previous = None
            if lastGreater != None:
                headNew.next = lastGreater
                lastGreater.previous = headNew
        lastLess = node
        countL += 1
    elif node.value >= partition:
        if countG == 0:
            node.next = None
            if lastLess != None:
                node.previous = lastLess
                lastLess.next = node
        lastGreater = node
        countG += 1

    node = nextNode

print "new list"
node = headNew
count = 0
while (node.next != headNew) and (node.next != None):
    print node.value
    node = node.next
    count += 1
print 'this is %i long'%count

