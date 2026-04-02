class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(path, index):
            if index == len(nums):
                ans.append(path[:])
                return
            if index > len(nums):
                return
            
            path.append(nums[index])
            backtrack(path, index+1)
            path.pop()
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(path, index+1)
        backtrack([], 0)
        return ans
            

        