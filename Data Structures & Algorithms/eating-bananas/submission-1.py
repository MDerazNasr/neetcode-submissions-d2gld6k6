class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        [1,4,3,2], h= 9
        [1,2,3,4]
        l k r
        '''
        
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l+r) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
