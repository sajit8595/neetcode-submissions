class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {')':'(', ']':'[', '}':'{'}
        for x in s:
            if x in '([{':
                st.append(x)
            elif st and st[-1] == d[x]:
                st.pop()
            else:
                return False

        if not st:
            return True
        return False