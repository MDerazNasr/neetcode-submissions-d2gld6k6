class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        ans, maxp = [], 0

        for i in nums:
            freq[i] += 1
        for k in range(k):
            maxp = max(freq, key=freq.get)
            ans.append(maxp)
            freq.pop(maxp)
        return ans