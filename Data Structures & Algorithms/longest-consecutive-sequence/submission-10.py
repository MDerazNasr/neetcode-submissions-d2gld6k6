class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        final = set(nums)
        n = 0
        longest = 0
        for i in final:
            count = 1
            nextval = i+1
            while nextval in final:
                count += 1
                nextval += 1
            longest = max(longest, count)
        return longest

            
