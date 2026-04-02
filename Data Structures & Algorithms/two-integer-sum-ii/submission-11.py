class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        there is one solution
        no repeated numbers
        index1 < index2
        O(1)
        [1,2,3,4] (3)
        1,4
        '''
        l, r = 0, len(numbers)-1

        while l < r:
            temp = numbers[l] + numbers[r]
            if temp > target:
                r -= 1
            elif temp < target:
                l += 1
            else:
                return [l+1,r+1]
