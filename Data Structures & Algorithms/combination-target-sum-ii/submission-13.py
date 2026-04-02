class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        1,2,2,4,5,6,9
              i
        '''
        
        ans = []
        candidates.sort()
        def backtrack(path, index):
            if sum(path) == target:
                ans.append(path[:])
                return
            if index >= len(candidates) or sum(path) > target:
                return
            
            path.append(candidates[index])
            backtrack(path, index+1)
            path.pop()
            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            backtrack(path, index+1)
        
        backtrack([], 0)
        return ans

        