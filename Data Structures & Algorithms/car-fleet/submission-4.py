class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        target=12
        position=[10,8,0,5,3]
        speed=[2,4,1,1,3]

        time = 1, 1, 12, 7, 9
        '''
        cars = []
        for i in range(len(speed)):
            cars.append([position[i],speed[i]])
        print(cars)

        cars.sort()
        times = {}
        stack = []
        for i in reversed(cars):
            time = (target - i[0]) / i[1]
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            
