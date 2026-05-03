class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        st = []
        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                currPos = st.pop()
                ans[currPos] = i - currPos
            st.append(i)
        return ans