class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i in '+-*/':
                b = st.pop()
                a = st.pop()
                new = -1
                if i == '+': new = (a + b)
                elif i == '-': new = (a - b)
                elif i == '*': new = (a * b)
                elif i == '/':
                    # in python -neg divisions are weird
                    new = abs(a) // abs(b)
                    if abs(a)+abs(b) != a + b:
                        new = -new
                st.append(new)
            else:
                st.append(int(i))
        return st[0]