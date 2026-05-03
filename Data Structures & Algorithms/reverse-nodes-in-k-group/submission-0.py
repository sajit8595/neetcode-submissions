# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head):
            curr = None
            while head:
                temp = head.next
                head.next = curr
                curr = head
                head = temp
            return curr
        
        def revK(curr, ind, start):
            if not curr:
                return start
            if ind % k == 0:
                reverseK = revK(curr.next, ind+1, curr.next)
                curr.next = None
                revHead = reverse(start)
                start.next = reverseK
                return revHead
            return revK(curr.next, ind+1, start)

        return revK(head, 1, head)

