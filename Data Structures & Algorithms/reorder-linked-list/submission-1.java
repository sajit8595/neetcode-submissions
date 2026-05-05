/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {

    public ListNode reverse(ListNode head) {
        ListNode dummy = null;
        while (head != null) {
            ListNode nextHead = head.next;
            head.next = dummy;
            dummy = head;
            head = nextHead;
        }
        return dummy;
    }

    public void mergeAlternate(ListNode l1, ListNode l2) {
        while (l2 != null) {
            ListNode nextL1 = l1.next;
            ListNode nextL2 = l2.next;

            l1.next = l2;
            l2.next = nextL1;

            l1 = nextL1;
            l2 = nextL2;
        }
    }

    public void reorderList(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        fast = fast.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode head2 = reverse(slow.next) ;
        slow.next = null;

        mergeAlternate(head, head2);
    }
}
