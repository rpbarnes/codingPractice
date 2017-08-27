"""
This makes a linked list and then checks for a cycle in that linked list.

"""
import random

class linkedListNode:# {{{
    def __init__(self, value):
        self.next = None
        self.value = value
        self.previous = None# }}}

def createLinkedList(listLen=10,cycleStart=4,cycleEnd=3,makeCycle=True):# {{{
    """
    This creates a doubly linked list and returns the head of the list
    """
    print "list that is generated"
    for i in range(listLen):
        randVal=random.randint(0,100)
        #randVal=i
        if i==0:
            head = linkedListNode(randVal)
            previous = head
        else:
            currentItem = linkedListNode(randVal)
            previous.next = currentItem
            currentItem.previous = previous
            previous = currentItem
        if i==cycleStart:
            cycleStart = currentItem
        elif i==cycleEnd:
            cycleEnd = currentItem
        print randVal
#create the cycle in the linked list. Isn't this a data error?? Should cycleEnd.previous = cycleStart?
    if makeCycle:
        cycleStart.next = cycleEnd
    return head# }}}

def findCycle(head):# {{{
    """ This finds if there is a cycled element in a linked list
    Returns True if cycled, False if no cycle is present in list
    This gives you way more information than you need.
    """
    print "finding looped item"
    currentItem = head
    previouslySeen = {currentItem:'headOfList'}
    for i in range(listLen):
        print currentItem.value
        seen = previouslySeen.get(currentItem)
        if seen == None:
            previouslySeen.update({currentItem:''})
        else:
            if seen=='headOfList':
                if i!=0:
                    print "found end of list that loops back to head of list"
            else:
                print "found loop at position %i"%i
                return True
        currentItem = currentItem.next
    return False# }}}

def findCycle1(head):
    count = 0
    """
    This loops through a linked list and finds if there is a cycle. This uses the fast and slow runner method.
    this ony gives you exactly what you need.
    """
    fastRunner = head.next
    slowRunner = head
    while True:
        if any((fastRunner == slowRunner,fastRunner.next.next==slowRunner.next)) and any((slowRunner != head, slowRunner.next != head)):
            print "found loop, with value %i"%fastRunner.value
            cycle = True
            break
        slowRunner = slowRunner.next
        fastRunner = fastRunner.next.next
        if slowRunner == head:
            print "found beginning of list"
            cycle = False
            break
        if fastRunner==None:
            print 'found end of list'
            cycle = False
            break
        count += 1
    print "did %i itterations"%count
    return cycle

        


head = createLinkedList(listLen = 110,cycleStart = 86, cycleEnd = 75,makeCycle=True)
cycled = findCycle1(head)



