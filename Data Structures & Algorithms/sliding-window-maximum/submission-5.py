from typing import List, Callable, Any

class SegmentTree:
    def __init__(self, data: List[int], merge_func: Callable[[Any, Any], Any], default_val: Any):
        self.data = data
        self.n = len(data)
        # Allocate memory for the segment tree (4 * n is the safe upper bound)
        self.tree = [default_val] * (4 * self.n)
        self.merge = merge_func
        self.default_val = default_val
        
        if self.n > 0:
            self._build(0, 0, self.n - 1)

    def _build(self, node: int, start: int, end: int) -> None:
        if start == end:
            # Leaf node will have a single element
            self.tree[node] = self.data[start]
            return
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        # Recursively build the left and right children
        self._build(left_child, start, mid)
        self._build(right_child, mid + 1, end)
        
        # Merge the children using the provided generic function
        self.tree[node] = self.merge(self.tree[left_child], self.tree[right_child])

    def query(self, L: int, R: int) -> Any:
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node: int, start: int, end: int, L: int, R: int) -> Any:
        # If the current range is completely outside the query range
        if R < start or L > end:
            return self.default_val
            
        # If the current range is completely inside the query range
        if L <= start and end <= R:
            return self.tree[node]
            
        # If the query range partially overlaps with the current range
        mid = (start + end) // 2
        left_val = self._query(2 * node + 1, start, mid, L, R)
        right_val = self._query(2 * node + 2, mid + 1, end, L, R)
        
        return self.merge(left_val, right_val)

    def update(self, idx: int, val: int) -> None:
        """Included for completeness in a generic tree, though not strictly needed for this problem."""
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node: int, start: int, end: int, idx: int, val: int) -> None:
        if start == end:
            self.tree[node] = val
            self.data[idx] = val
            return
            
        mid = (start + end) // 2
        if start <= idx <= mid:
            self._update(2 * node + 1, start, mid, idx, val)
        else:
            self._update(2 * node + 2, mid + 1, end, idx, val)
            
        self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
            
        # Initialize the generic Segment Tree
        # - merge_func: max
        # - default_val: float('-inf') (guarantees out-of-bounds nodes won't affect the maximum)
        seg_tree = SegmentTree(nums, max, float('-inf'))
        
        output = []
        # Slide the window from left to right
        for i in range(len(nums) - k + 1):
            # Query the maximum in the inclusive range [i, i + k - 1]
            window_max = seg_tree.query(i, i + k - 1)
            output.append(window_max)
            
        return output