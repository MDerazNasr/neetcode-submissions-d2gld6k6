class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2] -> 1. sort array
          i  l        r  -> 2p, going through all posibilties
                         -> no same triplets
        brute force - O(n3)
        two pointers + i - O(n2)

        triples cases:
        - [-1,-1.....]
            i --> move up i until its not the same
        - [-1,-1,1,1,....]
                i, l     r

        '''
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while l < r:
                check = nums[i] + nums[l] + nums[r]
                if check > 0:
                    r -= 1
                elif check < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ans
        