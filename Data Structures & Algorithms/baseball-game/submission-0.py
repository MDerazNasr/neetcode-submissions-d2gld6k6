class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == '+':
                print(stack)
                stack.append(stack[-1] + stack[-2])
            elif i == 'D':
                print(stack)
                stack.append(2 * stack[-1])
            elif i == 'C':
                print(stack)
                stack.pop()
            else:
                print(stack)
                stack.append(int(i))
        print(stack)
        return sum(stack)