class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            weight = x - y
            if weight != 0:
                heapq.heappush(heap, -weight)
        if len(heap) == 0:
            return 0
        return -heap[0]