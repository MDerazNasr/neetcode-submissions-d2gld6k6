class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        i = 0
        while i < len(nums):
            sum_list = 0
            hold = nums.pop(i)
            sum_list = math.prod(nums)
            final.append(sum_list)
            nums.insert(i, hold)
            i += 1
        return final
            
