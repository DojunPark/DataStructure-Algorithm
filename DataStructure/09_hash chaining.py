class HashChain:
    def __init__(self, m):
        self.size = m
        self.H = [singlyLinkedList() for _ in range(m)]

    def set(self, key, value=None):
        i = self.find_slot(key)
        v = self.H[i].search(key)
        if v == None:
            self.H[i].pushFront(key, value)
        else:
            v.value = value

    def remove(self, key):
        i = self.find_slot(key)
        v = self.H[i].search(key)
        return self.H[i].remove(v)




