class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #t,i val, index
        ans = [0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, index = stack.pop()
                ans[index] = i - index
            stack.append([t,i])
        return ans