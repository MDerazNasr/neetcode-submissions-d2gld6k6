class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            hold = nums.pop(i)
            prod = math.prod(nums)
            ans.append(prod)
            nums.insert(i, hold)
        return ans