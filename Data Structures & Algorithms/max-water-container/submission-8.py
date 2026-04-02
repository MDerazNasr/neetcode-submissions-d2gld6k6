class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        area = (r-1)*min(height)

        '''
        maxArea = 0
        l,r = 0, len(heights)-1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            maxArea = max(maxArea, area)
        return maxArea