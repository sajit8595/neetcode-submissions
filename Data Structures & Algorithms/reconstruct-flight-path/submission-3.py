from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # 1. Build adjacency list and sort normally (ascending)
        tickets.sort()
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)
            
        res = ["JFK"]
        
        def dfs(src):
            # Base case: if we used all tickets, we found the path
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                # Choose an edge
                adj[src].pop(i)
                res.append(v)
                
                # Explore
                if dfs(v):
                    return True
                
                # Undo choice (backtrack)
                adj[src].insert(i, v)
                res.pop()
                
            return False
            
        dfs("JFK")
        return res