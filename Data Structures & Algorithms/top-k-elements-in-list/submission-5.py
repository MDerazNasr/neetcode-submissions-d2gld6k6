class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = defaultdict(int)
        maxP = 0
        ans = []
        for i in nums:
            maps[i] += 1
        
        # for i,n in enumerate(maps.items()):
        for i in maps.items():
            maxT = max(maps, key=maps.get)
            ans.append(maxT)
            maps[maxT] = 0
            if len(ans) == k:
                return ans
        
        
        # for i in maps:
        #     maxP = max(maxP, i)
        #     ans.append(maxP)
        #     if len(ans) == k:
        #         return ans
