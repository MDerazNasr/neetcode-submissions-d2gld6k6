class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.runningSum = 0
        self.size = size

    def next(self, val: int) -> float:
        self.q.append(val)
        self.runningSum += val
        if len(self.q) > self.size:
            self.runningSum -= self.q.popleft()
        return self.runningSum / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
