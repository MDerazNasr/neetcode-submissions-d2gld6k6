class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1

        for i in range(len(numbers)):
            check = numbers[l] + numbers[r]
            if check == target:
                return [l+1, r+1]
            elif check > target:
                r -= 1
            else:
                l += 1
        return
        