class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [3,4,5,6,1,2]
         l   m      r
         x
        '''
        l, r = 0, len(nums)-1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] <= nums[r]:
                r = m - 1
            else:
                l = m + 1
        return res



