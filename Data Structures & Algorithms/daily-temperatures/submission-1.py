class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        ans = [0 for i in range(n)]

        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                x = st.pop()
                ans[x] = i - x
            st.append(i)
        
        return ans