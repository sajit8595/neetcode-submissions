class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        def recur(ind, path, currSum):
            if currSum == target:
                ans.append(path[:])
                return

            if ind == n:
                return
                
            if currSum + candidates[ind] <= target:
                path.append(candidates[ind])
                recur(ind+1, path, currSum + candidates[ind])
                path.pop()
            ind2 = ind
            while ind2 < n and candidates[ind2] == candidates[ind]:
                ind2 += 1
            recur(ind2, path, currSum)
        
        recur(0, [], 0)
        return ans