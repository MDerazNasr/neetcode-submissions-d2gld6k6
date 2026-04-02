class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {'}':'{', ']':'[', ')':'('}

        for i in s:
            if i in closed:
                if stack and stack[-1] == closed[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        else:
            return False
            
        