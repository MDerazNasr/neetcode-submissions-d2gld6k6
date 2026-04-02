class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1
        final = []

        while left < right:
            check = numbers[left] + numbers[right]
            if check == target:
                if numbers[left] < numbers[right]:
                    final.append(left+1)
                    final.append(right+1)
                    return final
                else:
                    final.append(right+1) 
                    final.append(left+1)
                    return final
            elif check < target:
                left += 1
            else:
                right -= 1 

        return final

        