class Solution:
    def groupAnagrams(self, strings: List[string]) -> List[List[string]]:
        d = {}
        for string in strings:
            freq = [0]*26
            for ch in string:
                freq[ord(ch) - ord('a')] += 1
            cal = ''
            for i in range(26):
                if freq[i] > 0:
                    st = chr(i + ord('a')) + str(freq[i])
                    cal += st
            if cal not in d:
                d[cal] = []
            d[cal].append(string)

        ans = [d[i] for i in d]
        return ans
