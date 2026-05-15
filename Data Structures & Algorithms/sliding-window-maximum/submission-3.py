from typing import List

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [float('-inf')] * (4 * self.n)
        self.nums = nums
        self.build(0, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            self.tree[node] = self.nums[l]
            return

        mid = (l + r) // 2
        self.build(2 * node + 1, l, mid)
        self.build(2 * node + 2, mid + 1, r)

        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return float('-inf')

        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2
        return max(
            self.query(2 * node + 1, l, mid, ql, qr),
            self.query(2 * node + 2, mid + 1, r, ql, qr)
        )


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        seg = SegmentTree(nums)
        return [
            seg.query(0, 0, len(nums) - 1, i, i + k - 1)
            for i in range(len(nums) - k + 1)
        ]