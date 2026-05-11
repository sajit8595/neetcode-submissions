class Solution:
    def __init__(self):
        self.ans = []

    def generateAll(self, ind, opens, close, path, n):
        if ind == 2*n:
            self.ans.append(''.join(path))
            return
        if opens < n:
            path.append('(')
            self.generateAll(ind+1, opens+1, close, path, n)
            path.pop()
        if close < opens:
            path.append(')')
            self.generateAll(ind+1, opens, close+1, path, n)
            path.pop()
        

    def generateParenthesis(self, n: int) -> List[str]:
        self.generateAll(0, 0, 0, [], n)
        return self.ans