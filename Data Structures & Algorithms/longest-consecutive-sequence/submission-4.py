class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        form sequences for only the starting value
        find starting value by checking if theres one smaller
        count by finding O(1)
        use map
        '''
        if len(nums) == 0:
            return 0
        count = 1
        final = []
        maps = set()
        for i in nums:
            maps.add(i)
        print(maps)
        
        for i in nums:
            check = i-1
            if check in maps:
                continue
            else:
                # print(check)
                # starters.append(i)
                # for l in starters:
                next_val = i
                # print(next_val)
                l = 0
                count = 1
                # while l < len(nums):
                next_val += 1
                while next_val in maps:
                    count += 1  
                    print(next_val, count)
                    next_val += 1
                    # l += 1   
                final.append(count)   
        return max(final)
        