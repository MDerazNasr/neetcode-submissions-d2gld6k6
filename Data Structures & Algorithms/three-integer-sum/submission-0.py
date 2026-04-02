class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #conditions - sum must be 0
        # no duplicates

        
        #step 3 - skip duplicate
        #step 4 - select b,c
        #step 5 - iterate (skip over duplicates/incorrect values)
        #step 6 - return

        nums.sort()#step 1 - sort it to avoid duplicates easier
        final = []
        #step 2 - select value a (first triplet)
        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    final.append([nums[i],nums[left],nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return final
                

            






        