class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        #Transpose
        # reflect over diagonal, basically swap [i][j] with [j][i]
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #Reflection over line in the middle
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j -1], matrix[i][j]
        
       
       