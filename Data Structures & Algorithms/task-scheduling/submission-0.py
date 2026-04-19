class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        tasks = [B,A,C,C,A,A]
        count = [B:2, A:3 , C:2]
        maxHeap = [-2, -3, -2] --> [-3,-2,-2]
        time = 0
        q = []

        '''
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time: 
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
            
         




        
        