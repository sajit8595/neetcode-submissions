# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(curr):
            if not curr or not curr.next:
                return curr
            reverseNode = reverse(curr.next)
            lastElement = curr.next
            lastElement.next = curr
            curr.next = None
            return reverseNode

        return reverse(head)

            

        dummy = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = dummy
            dummy = curr
            curr = temp
        return dummy