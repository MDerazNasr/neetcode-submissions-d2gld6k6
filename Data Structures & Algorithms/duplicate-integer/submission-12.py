class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums = Counter(nums)

        for i in nums:
            if nums[i] > 1:
                return True
        return False 
        