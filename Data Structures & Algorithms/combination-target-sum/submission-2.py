class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(index, path):
            if sum(path) == target:
                ans.append(path[:])
                return
            if index >= len(nums) or sum(path) > target:
                return
            
            path.append(nums[index])
            backtrack(index, path)
            path.pop()
            backtrack(index+1, path)
        backtrack(0,[])
        return ans
