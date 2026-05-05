class Solution {

    public boolean checkIfPossible(int mid, int[] piles, int h) {
        int currH = 0;
        for (int i = 0; i < piles.length; i++) {
            int reqH = (piles[i] + mid - 1) / mid;
            currH += reqH;
            if (currH > h) {
                return false;
            }
        }
        return true;
    }

    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = Arrays.stream(piles).max().orElse(-1);
        int ans = 0;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (checkIfPossible(mid, piles, h)) {
                ans = mid;
                high = mid-1;
            } else {
                low = mid+1;
            }
        }
        return ans;
    }
}
