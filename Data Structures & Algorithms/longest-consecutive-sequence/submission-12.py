class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sort = set(nums)
        longest = 0
        
        for i in nums:
            counter = 1
            next_val = i + 1
            while next_val in nums:
                counter += 1
                next_val +=1 
            longest = max(longest, counter)

        return longest