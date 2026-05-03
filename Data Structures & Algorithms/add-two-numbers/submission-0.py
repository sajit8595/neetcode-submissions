# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        curr = dummyNode
        rem = 0
        while l1 or l2 or rem > 0:
            l1Val = l2Val = 0
            if l1:
                l1Val = l1.val
                l1 = l1.next
            if l2:
                l2Val = l2.val
                l2 = l2.next
            
            tot = (l1Val + l2Val + rem)
            rem = tot // 10
            val = tot % 10
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummyNode.next

