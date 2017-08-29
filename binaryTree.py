"""
This implements a sorted binary tree data structure.

This implements the tree as a set which does not keep the store any duplicate values

To do:
    drawTree function to make a plot of the tree with all linkages and values
    shouldPivot function to determine if the tree should pivot to consolidate depth
    pivotTree function to pivot tree about a certain node
    deleteValue function to delete a value from the tree

"""
import random
from drawtree import draw_level_order

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.value = None
        self.left = None
        self.right = None

    def hasChildren(self):
        if self.right or self.left:
            return True

class Tree:
    def __init__(self):
        self.head = Node(None)
        self.maxLeafDepth = 0

    def insert(self, value):
        """
        Inserts value into tree in correctly sorted position. Call as treeInstance.insert(value). value is type int.
        
        You might come back and do this recursively just for practice.
        """
        if type(value) != int:
            raise ValueError("value must be type int")
        if not self.head.value:
            "insert at head if doesn't exist"
            self.head.value = value
        else:
            "find where to insert value"
            node = self.head
            depth = 0
            while True:
                if value < node.value:
                    if not node.left:
                        newNode = Node(node)
                        node.left = newNode
                        newNode.value = value
                        break
                    else:
                        node = node.left # this continues the while loop with the new node.
                elif value > node.value:
                    if not node.right:
                        newNode = Node(node)
                        node.right = newNode
                        newNode.value = value
                        break
                    else:
                        node = node.right
                else:
                    break
                depth += 1
            if depth > self.maxLeafDepth:
                self.maxLeafDepth = depth
    
    def findValue(self, value):
        "this finds the node that contains the corresponding value. Returns the node"
        return self._findValue(value, self.head)

    def _findValue(self, value, node):
        if node and node.value:
            if value < node.value:
                return self._findValue(value, node.left)
            elif value > node.value:
                return self._findValue(value, node.right)
            elif value == node.value:
                return node

        else:
            print "%i not found in tree"%value
            return None

    
    def findFullDepth(self):
        "This finds the depth of the deepest full level in the tree. Returns (int) equal to lowest fully occupied level"
        self.lowestFullLevel = None
        self._findFullDepth(self.head, 0)
        return self.lowestFullLevel

    def _findFullDepth(self, node, count):
        "This needs to run any time I want to know the deepest full level. How can you keep track of this nicely on addition?"
        if node:
            if self.lowestFullLevel:
                if self.lowestFullLevel > count:
                    self._findFullDepth(node.left, count + 1)
                    self._findFullDepth(node.right, count + 1)
            else:
                self._findFullDepth(node.left, count + 1)
                self._findFullDepth(node.right, count + 1)
        else:
            if self.lowestFullLevel: 
                if self.lowestFullLevel > count:
                    self.lowestFullLevel = count
            else:
                self.lowestFullLevel = count

    def minNode(self):
        return self._minNode(self.head)

    def _minNode(self,node):
        if node.left:
            return self._minNode(node.left)
        else:
            return node
    
    def nodeLeft(self, node):
        return node.left

    def nodeRight(self, node):
        return node.right

    def drawTree(self):
        """ This package I'm using doesn't work. It says the tree is way longer than it is and it's also unsorted. I'd rather show it in a plot than in the command line. """
        self.drawString = ''
        self._drawTree(self.head)
        print self.drawString
        draw_level_order(self.drawString)

    def _drawTree(self,node):
        "returns a list to draw the tree with the package drawtree"
        if node:
            if self.drawString == '':
                self.drawString += '%i'%node.value
            else:
                self.drawString += ',%i'%node.value
            self._drawTree(node.left)
            self._drawTree(node.right)
        else:
            self.drawString += ',#'

    def printFromHead(self):
        "prints the tree from top down left to right. This doesn't really do what I want it to do."
        self._printFromHead(self.head)

    def _printFromHead(self, node):
        if node:
            if not node.parent:
                print node.value
            else:
                if node.left and node.right:
                    print node.left.value, node.right.value
                elif node.left:
                    print node.left.value, ' #'
                elif node.right:
                    print '# ', node.right.value 
            self._printFromHead(node.left)
            self._printFromHead(node.right)

    def printTree(self):
        "called by user to print the tree"
        self._printTree(self.head)

    def _printTree(self,node):
        if node:
            self._printTree(node.left)
            print node.value
            self._printTree(node.right)
        else:
            return



# test the tree
bt = Tree()
for i in range(100):
    bt.insert(random.randint(0,100))

bt.printTree()

print "the depth is"
print bt.findFullDepth()
print "the minimum is %i" %bt.minNode().value

#print "looking for value 92"
#print "found %i" %bt.findValue(92).value
