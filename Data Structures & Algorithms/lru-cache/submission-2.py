class Node:
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.lookup = {}

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1

        node = self.lookup[key]
        self._moveToFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.lookup:
            if len(self.lookup) == self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.lookup[lru.key]

            newNode = Node(key, value)
            self._addToFront(newNode)
            self.lookup[key] = newNode
        else:
            node = self.lookup[key]
            node.val = value
            self._moveToFront(node)
    
    def _moveToFront(self, node):
        self._remove(node)
        self._addToFront(node)
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _addToFront(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        