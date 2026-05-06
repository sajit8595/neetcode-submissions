class Node {
    int val;
    int key;
    Node next;
    Node prev;

    Node(int val, int key) {
        this.val = val;
        this.key = key;
    }
}

class LRUCache {
    int cap;
    Map<Integer, Node> lookup = new HashMap<>();
    Node head;
    Node tail;
    int currCap;

    public LRUCache(int capacity) {
        this.cap = capacity;
        this.head = null;
        this.tail = null;
        this.currCap = 0;
    }

    public void remove(Node node) {
        if (node.prev != null) {
            node.prev.next = node.next;
        } else {
            this.head = node.next;
        }

        if (node.next != null) {
            node.next.prev = node.prev;
        } else {
            this.tail = node.prev;
        }

        node.next = null;
        node.prev = null;

        this.currCap -= 1;
        this.lookup.remove(node.key);
    }

    public void addOnTop(Node node) {

        if (this.head == null) {
            this.head = node;
            this.tail = node;
        } else {
            this.head.prev = node;
            node.next = this.head;
            this.head = node;
        }

        this.currCap += 1;
        this.lookup.put(node.key, node);
    }
    
    public int get(int key) {
        if (lookup.containsKey(key)) {
            Node node = lookup.get(key);
            remove(node);
            addOnTop(node);
            return node.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if (lookup.containsKey(key)) {
            Node node = lookup.get(key);
            node.val = value;
            remove(node);
            addOnTop(node);
        } else {
            if (this.currCap >= this.cap) {
                remove(this.tail);
            }
            addOnTop(new Node(value, key));
        }
    }
}
