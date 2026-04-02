class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        cant use num twice 
        
        return two integers
        i1 != i2

        sorted smallest to biggest
        [1,2,3,4], 6
        1+4 = 5 (6,7), (3,2)
        1+4 = 5 (4,3), (6,7) 


        '''
        l, r = 0, len(numbers)-1
        
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            else: 
                return [l + 1, r + 1]
        return []
        