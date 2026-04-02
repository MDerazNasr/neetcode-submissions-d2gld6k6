class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        [-1,0,2,4,6,8]
                  l r

        '''
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            print(l, r, m)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return r + 1
        



        