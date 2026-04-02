class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(path, index):
            if sum(path) == target:
                ans.append(path[:])
                return
            if index >= len(nums) or sum(path) > target:
                return 
            
            path.append(nums[index])
            backtrack(path, index)
            path.pop()
            backtrack(path, index+1)
        
        backtrack([], 0)
        return ans
        