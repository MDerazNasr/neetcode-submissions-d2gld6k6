class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        g = defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def dfs(node):
            curr_state = states[node]
            if curr_state == VISITING:
                return False
            elif curr_state == VISITED:
                return True

            states[node] = VISITING
            
            for neighbor in g[node]:
                if not dfs(neighbor):
                    return False
            
            states[node] = VISITED
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
        