class Solution:
    def isValid(self, s: str) -> bool:
        
        closed = {'}': '{', ']':'[', ')':'('}
        stack = []

        for i in s: 
            if i in closed:
                if stack and closed[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if not stack:
            return True
        else:
            return False