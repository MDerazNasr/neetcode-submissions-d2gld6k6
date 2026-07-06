class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0

        for i in nums:
            count = 1
            nextVal = i + 1
            while nextVal in nums:
                count += 1
                nextVal += 1
            ans = max(ans, count)
        return ans
        