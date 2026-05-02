class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def bisect_left(tar):
            l, r = 0, len(st)-1
            while l < r:
                mid = (r + l) // 2
                if st[mid] < tar:
                    l = mid+1
                else:
                    r = mid
            return l
        
        st = []
        for n in nums:
            if not st or st[-1] < n:
                st.append(n)
            else:
                ind = bisect_left(n)
                st[ind] = n
        return len(st)