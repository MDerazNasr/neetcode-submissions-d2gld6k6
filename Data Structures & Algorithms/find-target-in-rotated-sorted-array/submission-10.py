class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [3,4,5,6,1,2]
             l.  m  r
        '''
        l,r = 0, len(nums)-1
        while l < r:
            m = (l+r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else: 
                r = m

        if l == 0:
            l, r = 0, len(nums)-1
        elif target >= nums[0] and target <= nums[l-1]:
            #we are in the left side
            l, r = 0, l-1
        else:
            #l stays the same
            l, r = l, len(nums)-1
        
        while l <= r:
            m = (l+r) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1

