class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] #(val, index)
        index = 0
        ans = []

        for i in points: 
            euc = math.sqrt((i[0]-0)**2 + (i[1]-0)**2)
            heapq.heappush(heap, (euc, i)) #nlogn
        print (heap)
        
        while index < k:
            euc, x = heapq.heappop(heap)
            ans.append(x)
            index += 1
        
        return ans