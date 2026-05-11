class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < stones.length; i++) {
            pq.offer(stones[i]);
        }

        while (pq.size() > 1) {
            int high1 = pq.poll();
            int high2 = pq.poll();
            if (high1 != high2) {
                pq.offer(high1 - high2);
            }
        }

        return pq.isEmpty() ? 0 : pq.peek();
    }
}