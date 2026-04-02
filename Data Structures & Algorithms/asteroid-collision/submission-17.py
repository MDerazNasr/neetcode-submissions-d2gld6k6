class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        right - 2
        left. - -1
        '''
        left, right = [], []

        for i, v in enumerate(asteroids):
            if v > 0:
                right.append([i,v])
            else:
                left.append([i,v])
            
            while left and right:
                if left[-1][0] < right[-1][0]:
                    break
                elif abs(left[-1][1]) == abs(right[-1][1]):
                    left.pop()
                    right.pop()
                elif abs(left[-1][1]) > abs(right[-1][1]):
                    right.pop()
                else:
                    left.pop()
        final = left + right
        final.sort()
        ans = []
        for i in final:
            ans.append(i[1])
        return ans
        