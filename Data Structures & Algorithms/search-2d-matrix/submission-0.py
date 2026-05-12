class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        # 3, 4
        low = 0; high = n*m-1

        # 6
        # row = 6 / 4 (m) = 1
        # col = 6 % 4 (m) = 2
        while low <= high:
            mid = (low + high) // 2
            midR = mid // m
            midC = mid % m
            if matrix[midR][midC] == target:
                return True
            if matrix[midR][midC] > target:
                high = mid-1
            else:
                low = mid+1

        return False
