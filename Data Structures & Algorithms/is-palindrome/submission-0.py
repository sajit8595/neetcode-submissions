class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(i):
            return ('a' <= s[i] and s[i] <= 'z') or ('A' <= s[i] and s[i] <= 'Z') or ('0' <= s[i] and s[i] <= '9')

        n = len(s)
        i = 0
        j = n-1
        while i < j:
            if not isAlphaNumeric(i):
                i += 1
            elif not isAlphaNumeric(j):
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
                