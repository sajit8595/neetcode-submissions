class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # find median 
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2

        median = (n + 1) // 2

        low = 0
        high = n1

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = median - mid1

            l1, r1 = mid1-1, mid1
            l2, r2 = mid2-1, mid2

            l1E = nums1[l1] if l1 >= 0 else -float('inf')
            r1E = nums1[r1] if r1 < n1 else float('inf')
            l2E = nums2[l2] if l2 >= 0 else -float('inf')
            r2E = nums2[r2] if r2 < n2 else float('inf')

            if l1E <= r2E and l2E <= r1E:
                left = max(l1E, l2E)
                if n & 1:
                    return float(left)
                right = min(r1E, r2E)
                return (left + right) / 2.0
            elif l1E > r2E:
                high = mid1-1
            else:
                low = mid1+1

        return -1
