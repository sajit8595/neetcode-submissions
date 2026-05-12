class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ans = self.findValueForTimestamp(self.keys.get(key, []), timestamp)
        return ans[0] if ans else ""
    
    def findValueForTimestamp(self, arr, target):
        # lowerBound = [1, 1, 1] = 0th ind
        # upperBound = [1, 1, 1] = 3rd ind
        low = 0; high = len(arr)-1
        ans = []
        while low <= high:
            mid = (low + high) // 2
            if arr[mid][1] == target:
                return arr[mid]
            if arr[mid][1] < target:
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans
