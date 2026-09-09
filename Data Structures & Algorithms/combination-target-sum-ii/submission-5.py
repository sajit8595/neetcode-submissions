class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []

        def recur(ind, path, curTot):
            if curTot == target:
                ans.append(path.copy())
                return

            for nInd in range(ind, n):
                if nInd > ind and candidates[nInd-1] == candidates[nInd]:
                    continue

                if curTot + candidates[nInd] > target:
                    return

                path.append(candidates[nInd])
                recur(nInd+1, path, curTot + candidates[nInd])
                path.pop()
            
        recur(0, [], 0)

        return ans

