class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(path, index):
            if index == len(s):
                ans.append(path[:])
                return
            
            for j in range(index, len(s)):
                if self.isPali(s, index, j):
                    path.append(s[index:j+1])
                    backtrack(path, j+1)
                    path.pop()
        backtrack([],0)
        return ans
    def isPali(self,s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -=1
        return True

        