class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path, openn, close):
            if len(path) == 2*n:
                ans.append(''.join(path[:]))
            
            if openn < n:
                path.append('(')
                backtrack(path, openn+1, close)
                path.pop()
            
            if close < openn:
                path.append(')')
                backtrack(path, openn, close+1)
                path.pop()
        
        backtrack([],0,0)
        return ans

        