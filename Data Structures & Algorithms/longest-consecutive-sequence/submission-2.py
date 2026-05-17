class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        ans = 0
        for n in nums:
            if not mp[n]:
                mp[n] = 1 + mp[n-1] + mp[n+1]
                mp[n - mp[n-1]] = mp[n]
                mp[n + mp[n+1]] = mp[n]
            ans = max(ans, mp[n])
        return ans
