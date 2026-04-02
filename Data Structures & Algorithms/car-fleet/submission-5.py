class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for car in range(len(position)):
            cars.append([position[car], speed[car]])
        
        cars.sort(reverse=True)
        stack = []
        for i in cars:
            pos, sp = i
            stack.append((target-pos)/sp)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            

        