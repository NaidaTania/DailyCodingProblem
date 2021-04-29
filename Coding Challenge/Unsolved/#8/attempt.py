class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.value = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()
    


# def univalCounter(root):


tree = Node(1)
tree.insert(1)
tree.insert(0)
tree.insert(1)
tree.insert(0)
tree.PrintTree()