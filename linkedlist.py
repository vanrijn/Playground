class LinkedListNode:

    def __init__(self, value):
        self._value = value
        self._childNode = None
        print "New LinkedListNode with value: %s" % str(value)

    def childNode(self):
        return self._childNode

    def setChildNode(self, node):
        self._childNode = node

    def value(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def __str__(self):
        return "{Value: %s}" % str(self._value)


class LinkedList:

    def __init__(self):
        self._rootNode = None
        self._lastNode = None
        self._size = 0

    def push_back(self, value):
        node = LinkedListNode(value)

        # If this is the first time adding a node, this will be our rootNode.
        # Otherwise append the new node to be lastNode's childNode
        if self._rootNode is None:
            print "Updating root node to %s" % node
            self._rootNode = node
        else:
            self._lastNode.setChildNode(node)

        self._lastNode = node
        self._size += 1

    def size(self):
        return self._size

    def count(self):
        numNodes = 0
        node = self._rootNode
        while node is not None:
            numNodes += 1
            node = node.childNode()

        return numNodes

    def print_all(self):
        print "My size is: %d" % self._size
        node = self._rootNode
        while node is not None:
            print "Node: %s" % node
            node = node.childNode()

    def remove(self, value):
        if self._size == 0:
            print "Can't remove value %s. I'm empty" % str(value)
            return

        if self._size == 1:
            self._rootNode.setValue(None)
            return

        node = self._rootNode
        parentNode = None

        while node is not None:
            if node.value() == value:
                print "Found node."
                break

            parentNode = node
            node = node.childNode()

        # We can only remove a node if we found one
        if node is None or node.value() != value:
            print "Sorry, couldn't remove value: %s (not found)" % str(value)
            return

        nextNode = node.childNode()

        # If we're removing our root node, update it to be the next node
        if parentNode is None:
            print("Removing root node %s and updating to new node: %s" %
                  (self._rootNode, nextNode))
            self._rootNode = nextNode
        elif self._lastNode is node:
            print("Removing the last node. Updating lastNode (%s) to parentNode (%s)" %
                  (self._lastNode, parentNode))
            # Make sure node is the last node, with no children
            assert node.childNode() is None
            # Make sure parentNode has node as its child
            assert parentNode.childNode() is node

            parentNode.setChildNode(None)
            self._lastNode = parentNode
        else:
            print("Parent node: %s, now joining to new child node: %s" %
                  (parentNode, nextNode))
            # Make sure parentNode has current node as its child already
            assert parentNode.childNode() is node

            parentNode.setChildNode(nextNode)

        self._size -= 1


list = LinkedList()

print "Trying to remove something from an empty list"
list.remove("something from an empty list")
print

print "Populating list"
list.push_back(1)
list.push_back(2)
list.push_back("chicken")
list.push_back(4)
list.push_back(5)
list.push_back("egg")
list.print_all()
expected = 6
assert list.size() == expected and list.count() == expected
print

print "Trying to remove something not in the list..."
list.remove("something not in the list")
list.print_all()
expected = 6
assert list.size() == expected and list.count() == expected
print

print "Removing first node (1)"
list.remove(1)
list.print_all()
expected = 5
assert list.size() == expected and list.count() == expected
print

print "Removing middle node (4)"
list.remove(4)
list.print_all()
expected = 4
assert list.size() == expected and list.count() == expected
print

print "Removing last node (egg)"
list.remove("egg")
list.print_all()
expected = 3
assert list.size() == expected and list.count() == expected
print

print "Adding more things to the list"
list.push_back("Old")
list.push_back("McDonald")
list.push_back("Had")
list.push_back("A")
list.push_back("Farm")
list.print_all()
expected = 8
assert list.size() == expected and list.count() == expected
print
