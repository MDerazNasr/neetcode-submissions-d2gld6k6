class MedianFinder:

    def __init__(self):
        self.left, self.right = [], []
        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.right and (-self.left[0] > self.right[0]):
            heapq.heappush(self.right, -heapq.heappop(self.left))
        
        #balancing sizes of each one, each list can be at most 1 item size bigger
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        
        if len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        
        if len(self.right) > len(self.left):
            return self.right[0]
        
        return (self.right[0] + -self.left[0]) / 2
        



       