class KthLargest {
    int k;
    PriorityQueue<Integer> pq;

    public KthLargest(int k, int[] nums) {
        this.pq = new PriorityQueue<>(k);
        this.k = k;

        for (int i=0; i<nums.length; i++) {
            add(nums[i]);
        }
    }
    
    public int add(int val) {
        pq.offer(val);
        if (pq.size() > this.k) {
            pq.poll();
        }
        return pq.peek();
    }
}
