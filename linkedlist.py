class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.childNode = None
		print "Hi there! I'm a LinkedListNode and my value is: %s" % value

	def childNode(self):
		return self.childNode

	def setChildNode(self, node):
		self.childNode = node

	def value(self):
		return self.value

	def setValue(self, value):
		self.value = value

class LinkedList:
	def __init__(self):
		self.rootNode = None
		self.lastNode = self.rootNode
		self.size = 0

	def push_back(self, value):
		node = LinkedListNode(value)

		# If this is the first time adding a node, this will be our rootNode.
		# Otherwise, set rootNode to be the parentNode
		if self.rootNode is None:
			self.rootNode = node
		else:
			self.lastNode.setChildNode(node)

		self.lastNode = node
		self.size += 1

	def print_all(self):
		node = self.rootNode
		while node is not None:
			print "Node value: %s" % str(node.value())
			node = node.childNode()

	def remove(self, value):
		if self.size == 0:
			print "Can't remove value %s. I'm empty" % str(value)
			return

		if self.size == 1:
			self.rootNode.setValue(None)
			return

		node = self.rootNode
		parentNode = None

		while node is not None:
			if node.value() == value:
				break

			parentNode = node
			node = node.childNode()

		# We can only remove a node if we found one
		if node.value() != value:
			print "Sorry, couldn't remove value: %s (not found)" % str(value)
			return

		parentNode.setChildNode(node.childNode())

		self.size -= 1


list = LinkedList()

# this will fail
print "Trying to remove something from an empty list"
list.remove("something from an empty list")
list.print_all()

print "Populating list"
list.push_back(1)
list.push_back(2)
list.push_back("chicken")
list.push_back(4)
list.push_back(5)
list.push_back("egg")
list.print_all()

# this will fail because it's not there
print "Trying to remove something not in the list..."
list.remove("something not in the list")
list.print_all()


# this should succeed
print "Removing first node (1)"
list.remove(1)
list.print_all()

# this should succeed
print "Removing middle node (4)"
list.remove(4)
list.print_all()
