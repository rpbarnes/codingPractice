"""
Given a mesh network and a graph data structure that connects all neighbors in the network find the quickest route between two nodes of the network.

If there is no path connecting the nodes return none and tell the user.

"""
from Queue import Queue

network = {
    'Min'     : ['William', 'Jayden', 'Omar'],
    'William' : ['Min', 'Noam'],
    'Jayden'  : ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren'     : ['Jayden', 'Omar'],
    'Amelia'  : ['Jayden', 'Adam', 'Miguel'],
    'Adam'    : ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel'  : ['Amelia', 'Adam', 'Liam', 'Nathan'],
}

def rebuildRoute(parent, target, previousNode):
    path = []
    path.append(target)
    node = previousNode.get(target)
    while node:
        path.append(node)
        node = previousNode.get(node)
    path.reverse()
    return path

def findRoute(parent, target, network):
    if parent == target:
        print "Sending message from %s to %s. Don't use network"%(parent, target)
        return None
    nodesToCheck = Queue()
    nodesToCheck.put(parent)
    previousNode = {parent: None}
    while not nodesToCheck.empty():
        node = nodesToCheck.get()
        neighbors = network.get(node) # get neighbors for last node in path
        if neighbors:
            for neighbor in neighbors:
                if neighbor == target:
                    # found target return list of nodes to target
                    previousNode.update({neighbor: node})
                    return rebuildRoute(parent, target, previousNode)
                else:
                    # add the next neighbor to check after all current neighbors to check.
                    if neighbor not in previousNode.keys():
                        nodesToCheck.put(neighbor)
                        previousNode.update({neighbor: node})
    
    print "did not find path from %s to %s"%(parent, target)
    return None


route = findRoute('Jayden', 'Adam', network)
print route
