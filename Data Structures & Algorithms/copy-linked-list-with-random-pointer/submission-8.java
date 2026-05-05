/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public void insertNodes(Node head) {
        while (head != null) {
            Node nextHead = head.next;
            head.next = new Node(head.val);
            head.next.next = nextHead;
            head = nextHead;
        }
    }

    public void copyRandoms(Node head) {
        while (head != null) {
            if (head.random != null) {
                head.next.random = head.random.next;
            }
            head = head.next.next;
        }
    }

    public Node getNewLinkedList(Node head) {
        Node ans = new Node(-1);
        Node curr = ans;
        while (head != null) {
            curr.next = head.next;
            head.next = head.next.next;

            curr = curr.next;
            head = head.next;
        }
        return ans.next;
    }

    public Node copyRandomList(Node head) {
        insertNodes(head);
        copyRandoms(head);
        return getNewLinkedList(head);
        // return head;
    }
}
