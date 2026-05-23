class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        ans = 0
        for op in operations:
            if op == 'D':
                st.append(st[-1] * 2)
                ans += st[-1]
            elif op == 'C':
                ans -= st.pop()
            elif op == '+':
                st.append(st[-1] + st[-2])
                ans += st[-1]
            else:
                st.append(int(op))
                ans += st[-1]
        return ans