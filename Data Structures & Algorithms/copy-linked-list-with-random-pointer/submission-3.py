"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def insertCopies(curr):
            while curr:
                if not curr:
                    return
                nxt = curr.next
                curr.next = Node(curr.val)
                curr.next.next = nxt
                curr = nxt
        
        def copyRandoms(curr):
            while curr:
                if not curr:
                    return
                if curr.random:
                    curr.next.random = curr.random.next
                curr = curr.next.next
        
        def getNewClone(curr):
            if not curr:
                return None
            head = curr.next
            
            while curr:
                cloneNode = curr.next
                curr.next = curr.next.next

                if curr.next:
                    cloneNode.next = curr.next.next

                curr = curr.next

            return head

        insertCopies(head)
        copyRandoms(head)
        return getNewClone(head)
        return head