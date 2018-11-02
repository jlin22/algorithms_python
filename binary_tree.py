class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = null
        self.right = null

class BinaryTree(object):
    def __init__(self, root):
        """Creates a tree with the value of root"""
        self.root = Node(root)

    def preorder_search(self, start, find_val):
