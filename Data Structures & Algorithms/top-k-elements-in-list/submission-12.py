class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counted = Counter(nums)
        max_val = 0
        ans = []

        for i in range(k):
            max_val = max(counted, key=counted.get)
            ans.append(max_val)
            counted.pop(max_val)
        return ans