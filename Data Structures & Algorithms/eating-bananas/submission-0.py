class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        [1,4,3,2], h = 9
        hours = 1+2+2+1 = 6

        [1,2,3,4], k = 2


        '''
        
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            hours = 0
            k = (l + r) // 2
            for p in piles:
                hours += math.ceil(p/k)
            if hours <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k + 1
        return res
        

    
        