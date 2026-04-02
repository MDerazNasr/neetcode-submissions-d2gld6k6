class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        k - banana / hour
        min hours taken is always len(piles)

        piles = [1,4,3,2], h = 9

        [1.........max(piles)] #we are not sorting piles
        [1, 2, 3, 4]
            l  k  r -> O(log n)

        1. what are we searching in
        2. how do we decide to move k up/down
        3. parameters for k
        '''
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            #calc k
            k = (l+r) // 2

            #hours taken for k
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/k)
            
            if total_time <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res



        