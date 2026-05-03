class DLL:
    def __init__(self, val, key, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.currLen = 0
        self.vis = {}

    def remove(self, node):
        del self.vis[node.key]
        self.currLen -= 1

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.next = None
        node.prev = None

    def addOnTop(self, node):
        self.vis[node.key] = node
        self.currLen += 1

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node      


    def get(self, key: int) -> int:
        if key in self.vis:
            node = self.vis[key]
            self.remove(node)
            self.addOnTop(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.vis[key].val = value
        else:
            if self.currLen >= self.capacity:
                self.remove(self.tail)
            self.addOnTop(DLL(value, key))