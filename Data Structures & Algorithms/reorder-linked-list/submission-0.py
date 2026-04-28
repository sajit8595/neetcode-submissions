# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            dummy = None
            while head:
                temp = head.next
                head.next = dummy
                dummy = head
                head = temp
            return dummy

        slow = fast = head
        fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        head1 = head
        head2 = reverse(mid.next)
        mid.next = None

        while head2:
            tempHead1 = head1.next
            tempHead2 = head2.next

            head1.next = head2
            head2.next = tempHead1

            head1 = tempHead1
            head2 = tempHead2
        
