"""
This keeps track of the maxima of a stack (really a list)

"""
import random

class Stack:
    """
    This is the list class that does all the fancy things I need my list to do...
    """

# initialize an empty list
    def __init__(self):
        self.items = []

# push a new item to the last index
    def push(self, item):
        self.items.append(item)

# remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

# see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

class MaxStack:

# initialize a Stack class for the items and for the max vals
    def __init__(self):
        self.stack = Stack()
        self.maxStact = Stack()

# push the new item to the stack and if the item is larger than the most recent max value push it to maxStact
    def push(self, item):
        self.stack.push(item)
        if not self.maxStact.items:
            self.maxStact.push(item)
        else:
            if int(item) > int(self.maxStact.peek()): # this is strange if I don't specify as int() a comp between 10 > 9 will return False
                self.maxStact.push(int(item))

# remove the last item from the list and check to see if the last item is the last item in maxStact, if so pop the last item out of maxStact.
    def pop(self):
        lastItem = self.stack.pop()
        if int(lastItem) == int(self.maxStact.peek()): 
            self.maxStact.pop()
        return lastItem

# return last element without removing it from list. Just call underlying class
    def peek(self):
        return self.stack.peek()

# return the last element of maxStact as this is the largest value currently in the stack
    def get_max(self):
        return self.maxStact.peek()

        

stack = MaxStack()
for i in range(10):
    stack.push(random.randint(0,10))

print "The values in the list are \n", stack.stack.items

for i in range(random.randint(0,5)):
    stack.pop()

print "The values in the list are \n", stack.stack.items
print stack.get_max()
