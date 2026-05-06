class Solution {

    public int recursion(int currDay, boolean iHold, int[] prices) {
        if (currDay >= prices.length) {
            return 0;
        }
        int skip = 0 + recursion(currDay+1, iHold, prices);
        if (iHold == true) {
            int sell = prices[currDay] + recursion(currDay+2, false, prices);
            return Math.max(sell, skip);
        } else {
            int buy = -prices[currDay] + recursion(currDay+1, true, prices);
            return Math.max(buy, skip);
        }
    }

    public int maxProfit(int[] prices) {
        int[][] dp = new int[prices.length+2][2];
        for (int currDay = prices.length-1; currDay >= 0; currDay--) {
            for (int iHold = 0; iHold < 2; iHold++) {
                int skip = 0 + dp[currDay+1][iHold];
                if (iHold == 1) {
                    int sell = prices[currDay] + dp[currDay+2][0];
                    dp[currDay][iHold] = Math.max(sell, skip);
                } else {
                    int buy = -prices[currDay] + dp[currDay+1][1];
                     dp[currDay][iHold] = Math.max(buy, skip);
                }
            }
        }
        return dp[0][0];
    }
}
