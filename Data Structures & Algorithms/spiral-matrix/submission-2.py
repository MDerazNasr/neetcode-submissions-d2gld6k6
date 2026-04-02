class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while left < right and top < bottom:

            #getting every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            #getting every i in the right column
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            '''
            Before I traverse the bottom row and left column, I need to check that there's
            still a valid region left. After shrinking the top and right boundaries, we might
            be down to a single row or single column with nothing left to process. Without
            this check, we'd double-count elements we already visited."
            '''
            if not (left < right and top < bottom):
                break
            
            #gettign every i in the bottom row
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            
            #getting every i in the left col
            for i in range(bottom - 1, top -1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
        