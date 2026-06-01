class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for fr, to in sorted(tickets, reverse = True):
            adj[fr].append(to)

        ans = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            ans.append(src)
        
        dfs("JFK")
        return ans[::-1]
        