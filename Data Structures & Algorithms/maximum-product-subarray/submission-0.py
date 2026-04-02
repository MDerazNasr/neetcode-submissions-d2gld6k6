class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_sum = 1
        max_sum = 1
        max_prod = nums[0]

        for i in nums:
            prev_min = min_sum
            prev_max = max_sum

            min_sum = min(i, prev_max*i, prev_min*i)
            max_sum = max(i, prev_max*i, prev_min*i)
            max_prod = max(max_prod, max_sum)
        
        return max_prod