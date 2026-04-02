class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hnums = {}
        for i in nums:
            if i in hnums:
                hnums[i] += 1
            else:
                hnums[i] = 1
        for i in hnums:
            if hnums[i] > 1:
                return True
        return False
        
        return True