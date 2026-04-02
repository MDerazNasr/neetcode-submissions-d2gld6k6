class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        form sequences for only the starting value
        find starting value by checking if theres one smaller
        count by finding O(1)
        use map
        '''
        final = []
        maps = set()
        
        if len(nums) == 0:
            return 0
       
        for i in nums:
            maps.add(i)
        
        for i in nums:
            check = i-1
            if check in maps:
                continue
            else:
                next_val = i
                count = 1
                next_val += 1
                while next_val in maps:
                    count += 1  
                    print(next_val, count)
                    next_val += 1  
                final.append(count)   
        return max(final)
        