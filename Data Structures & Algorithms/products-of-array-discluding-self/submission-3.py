class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            hold = nums.pop(i)
            prod = math.prod(nums)
            ans.append(prod)
            nums.insert(i, hold)
            i += 1
        return ans