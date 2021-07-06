class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)

    def preorder(self):
        if self != None:
            print(self.key)
            if self.left: self.left.preorder()
            if self.right: self.right.preorder()

    def inorder(self):
        if self != None:
            if self.left: self.left.inorder()
            print(self.key)
            if self.right: self.right.inorder()

    def postorder(self):
        if self != None:
            if self.left: self.left.postorder()
            if self.right: self.right.postorder()
            print(self.key)

    def __iter__(self):
        if self != None:
            # L
            if self.left != None:
                for elm in self.left:
                    yield elm
            # M
            yield self.key
            # R
            if self.right != None:
                for elm in self.right:
                    yield elm