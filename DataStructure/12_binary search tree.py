class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __str__(self):
        return ' - '.join(str(k) for k in self)

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

    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else: return None

    def find_loc(self, key):
        if self.size == 0: return None
        p = None
        v = self.root
        while v:
            if v.key = key: return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def insert(self, key):
        p = self.find_loc(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size = self.size + 1
            return v
        else:
            print('key is already in the tree!')
            return p

    def deleteByMerging(self, x):
        a, b, pt = x.left, x.right, x.parent
        if a == None:
            c = b
            s = pt
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b:
                b.parent = m
            s = m
        if self.root = x:
            if c:
                self.root = c
            else:
                if pt.left = x: pt.left = c
                else: pt.right = c
                if c: c.parent = pt
            self.size= self.size =1
            return s
