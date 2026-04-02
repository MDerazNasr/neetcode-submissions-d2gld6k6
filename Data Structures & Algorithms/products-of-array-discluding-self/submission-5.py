class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i,n in enumerate(nums):
            hold = nums.pop(i)
            curr_sum = math.prod(nums)
            ans.append(curr_sum)
            nums.insert(i, hold)
        return ans