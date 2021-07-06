# balanced binary search tree - AVL tree

class AVL(BST):
    def insert(self, key):
        v = super(AVL, self).insert(key)
        w = reebalance(x, y, z)
        if w.parent ==None:
            self.root = w
    def delete(self, x):
        v = super(AVL, self).deleteByCopying(u)
        while v != None:
            update v.height
            if v is not balanced:
                z = v
                if z.left.height >= z.right.height:
                    y = z.left
                else:
                    y = z.right
                if y.left.height >= y.right.height:
                    x = y.left
                else:
                    x = y.right
                v = rebalance(x, y, z)
            w = v
            v = v.parent
            self.root = w





