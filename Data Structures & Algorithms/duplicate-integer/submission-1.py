class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         h = len(nums) != len(set(nums))
         return h