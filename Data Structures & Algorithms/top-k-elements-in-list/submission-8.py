class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = defaultdict(int)
        ans = []
        for i in nums:
            maps[i] += 1
        
        for i in nums:
            maxT = max(maps, key=maps.get)
            ans.append(maxT)
            # maps[maxT] = 0
            maps.pop(maxT)
            if len(ans) == k:
                return ans
        
