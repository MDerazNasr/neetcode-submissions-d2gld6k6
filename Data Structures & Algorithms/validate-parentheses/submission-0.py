class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {"}": "{", "]":"[",")":"(" }

        for b in s:
            if b in closed:
                if stack and stack[-1] == closed[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        if not stack:
            return True
        else:
            return False

                
