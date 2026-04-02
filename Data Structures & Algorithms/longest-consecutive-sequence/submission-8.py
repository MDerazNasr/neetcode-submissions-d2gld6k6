class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        form sequences for only the starting value
        find starting value by checking if theres one smaller
        count by finding O(1)
        use map
        '''
        maps = set(nums)
        longest = 0
        if len(nums) == 0:
            return 0
       
        for i in nums:
            if i-1 in maps:
                continue
            else:
                count = 1
                next_val = i+1
                while next_val in maps:
                    count += 1  
                    next_val += 1  
                longest = max(count, longest)   
        return longest
        