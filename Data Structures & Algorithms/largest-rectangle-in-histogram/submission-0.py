class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                h, index = stack.pop()
                area = (i - index) * h
                maxArea = max(maxArea, area)
                start = index
            stack.append((height, start))
        
        while stack:
            h2, i2 = stack.pop()
            w2 = len(heights) - i2
            maxArea = max(maxArea, h2*w2)
        
        return maxArea