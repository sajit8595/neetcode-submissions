class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ''
        for string in strs:
            newSt = str(len(string)) + '@'
            st += (newSt + string)
        return st

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            curr = i
            while s[curr] != '@':
                curr += 1
            start = curr + 1
            end = curr + int(s[i:curr]) + 1
            ans.append(s[start:end])
            i = end
        return ans
