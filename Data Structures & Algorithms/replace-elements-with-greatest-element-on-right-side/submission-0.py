class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxEle = arr[n-1]
        arr[n-1] = -1
        for i in range(n-2, -1, -1):
            temp = arr[i]
            arr[i] = maxEle
            maxEle = max(maxEle, temp)
        return arr