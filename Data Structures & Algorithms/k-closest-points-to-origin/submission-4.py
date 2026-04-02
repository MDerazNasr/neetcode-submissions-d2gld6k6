class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        index = 0
        ans = []

        for i in points:
            euc = math.sqrt((i[0]-0)**2 + (i[1]-0)**2)
            heap.append((euc,i))
        heapq.heapify(heap)
        while index < k:
            val, coor = heapq.heappop(heap)
            ans.append(coor)
            index += 1
        return ans
        