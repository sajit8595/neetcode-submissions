# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # nth from end = travel xlen-n length from start
        # total = n + xlen - n = xlen
        # move first pointer from start to N, rem = xlen-n
        # now move second pointer from start till first pointer reaches end
        # i.e second moved xlen-n times
        # 4 eles, 2 from end - 1 2 3 4
        # fast = 3 ; slow = 1
        # fast = 3, 4, None ; slow = 1, 2, 3
        # stop slow at 2?

        fast = head
        while n:
            fast = fast.next
            n -= 1

        if not fast:
            return head.next

        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head