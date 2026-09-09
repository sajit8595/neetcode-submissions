class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort() #

        n = len(candidates)
        ans = []

        def recur(ind, path, curTot):
            if curTot > target:
                return

            if ind == n:
                if curTot == target:
                    ans.append(path[:])
                return
            
            ind1 = ind
            while ind1 < n and candidates[ind] == candidates[ind1]:
                ind1 += 1
            recur(ind1, path, curTot)

            path.append(candidates[ind])
            curTot += candidates[ind]
            recur(ind+1, path, curTot)
            curTot -= candidates[ind]
            path.pop()
        
        recur(0, [], 0)

        return ans