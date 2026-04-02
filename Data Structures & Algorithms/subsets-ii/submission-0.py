class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def backtrack(index, path):
            if index == len(nums):
                res.append(path[:])
                return
            # for x in nums:
            #     path.append(x)
            #     backtrack(index+1, path)
            #     path.pop()

            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index+1, path)
        
        backtrack(0,[])
        return res