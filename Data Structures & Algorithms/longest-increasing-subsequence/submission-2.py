class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def findJustGreaterInd(arr, tar):
            low = 0
            high = len(arr) - 1

            ind = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= tar:
                    ind = mid
                    high = mid-1
                else:
                    low = mid+1
            return ind

        st = []
        for x in nums:
            if not st or st[-1] < x:
                st.append(x)
            else:
                justGreaterInd = findJustGreaterInd(st, x)
                st[justGreaterInd] = x

        return len(st)