class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        k = # bananas eaten per hour
        k = 1.....max(piles) 
        min of h = len(piles)

        piles = [1,4,3,2], h = 9
        
        [1,2,3,4] #1....max(piles)
        l   m   r

        1. we figure out the range we're searching in
        2. compute mid (k)
        3. calculate h
        4. find the smallest m
        '''
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            k = (l+r) // 2

            time = 0
            for i in piles:
                time += math.ceil(i/k)
            
            if time <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res
            

