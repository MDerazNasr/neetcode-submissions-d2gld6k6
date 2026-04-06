class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        left, right = [], []
        for i,v in enumerate(asteroids):
            if v < 0:
                left.append([i, v])
            else:
                right.append([i,v])
            
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
        final = right + left
        final.sort()
        print(final)
        ans = []
        for i in final:
            ans.append(i[1])
        return ans
            
        


                
        