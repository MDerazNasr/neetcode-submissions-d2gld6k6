class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        area = width * height
             = (r - l) * min(h[l], h[r])

        [1,7,2,5,4,7,3,6]
           l            r
        '''
        maxArea = 0
        l,r = 0, len(heights)-1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
            maxArea = max(maxArea, area)
        return maxArea
