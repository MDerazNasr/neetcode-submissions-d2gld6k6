class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = set(nums)
        longest = 0
        for i in nums:
            count = 1
            next_val = i+1
            while next_val in res:
                count += 1
                next_val += 1
            longest = max(longest, count)
        return longest
        