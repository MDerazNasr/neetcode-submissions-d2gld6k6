class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        print(nums)

        n = len(nums)
        while len(ans) < n:
            hold = nums.pop(0)
            prod = math.prod(nums)
            ans.append(prod)
            nums.append(hold)
        
        return ans