class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucketFreq = [[] for i in range(n+1)]
        for key in count:
            bucketFreq[count[key]].append(key)
        
        ans = []
        for i in range(n, -1, -1):
            for num in bucketFreq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans