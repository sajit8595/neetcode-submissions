class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for x in s:
            if x in '([{':
                st.append(x)
            elif st:
                if x == ')' and st[-1] == '(':
                    st.pop()
                elif x == '}' and st[-1] == '{':
                    st.pop()
                elif x == ']' and st[-1] == '[':
                    st.pop()
                else:
                    return False
            else:
                return False
        if not st:
            return True
        return False