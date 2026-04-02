class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        ans = []
        max_val = 0
        for i in nums:
            freq[i] += 1
        for k in range(k):
            max_val = max(freq, key=freq.get)
            ans.append(max_val)
            freq.pop(max_val)
        return ans


        