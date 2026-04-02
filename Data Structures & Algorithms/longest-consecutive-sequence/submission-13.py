class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        maxSeq = 0

        for i in nums:
            count = 1
            nextVal = i + 1
            while nextVal in nums:
                count += 1
                nextVal += 1
            maxSeq = max(maxSeq, count)
        return maxSeq


        