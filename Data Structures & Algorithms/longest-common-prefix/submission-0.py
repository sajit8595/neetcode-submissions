class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        strN = len(strs[0])

        for i in range(1, n):
            a = strs[i-1]
            b = strs[i]
            for j in range(strN):
                if j < len(a) and j < len(b) and a[j] == b[j]:
                    continue
                else:
                    strN = j
                    break

        return strs[0][:strN]