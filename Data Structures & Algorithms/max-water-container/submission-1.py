class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            # Find the height and width
            h = min(heights[left], heights[right])
            w = right - left
            area = h * w
            max_water = max(max_water, area)

            # Move the pointer with smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water
        


