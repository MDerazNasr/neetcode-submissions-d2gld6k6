class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        def backtrack(index, path):
            if index == len(nums):
                res.append(path[:])

            for x in nums:
                if x not in path:
                    path.append(x)
                    backtrack(index+1,path)
                    path.pop()
        
        backtrack(0,[])
        return res
        