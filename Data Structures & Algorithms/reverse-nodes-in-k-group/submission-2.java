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
        ListNode curr = null;
        while (head != null) {
            ListNode nxt = head.next;
            head.next = curr;
            curr = head;
            head = nxt;
        }
        return curr;
    }

    public ListNode reverseK(ListNode curr, ListNode head, int counter, int k) {
        if (curr == null) {
            return head;
        }
        if (counter % k == 0) {
            ListNode nextReverseK = reverseK(curr.next, curr.next, counter + 1, k);
            curr.next = null;
            ListNode reverseHead = reverse(head);
            head.next = nextReverseK;
            return reverseHead;
        } else {
            return reverseK(curr.next, head, counter + 1, k);
        }
    }

    public ListNode reverseKGroup(ListNode head, int k) {
        return reverseK(head, head, 1, k);
    }
}
