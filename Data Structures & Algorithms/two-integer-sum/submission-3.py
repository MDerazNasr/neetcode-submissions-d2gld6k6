class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}
        for i, n in enumerate(nums):
            c = target - n
            if c in h:
                return [nums.index(c), i]
            h[n] = i
        return
