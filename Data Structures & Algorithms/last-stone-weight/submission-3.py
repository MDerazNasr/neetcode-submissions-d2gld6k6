class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            

            weight = y - x
            print(y, x, weight)
            if weight != 0:
                heapq.heappush(heap, -weight)
        if not heap:
            return 0
        else:
            return abs(heap[0])


        