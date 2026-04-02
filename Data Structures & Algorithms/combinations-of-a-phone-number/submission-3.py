class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        ans = []

        def backtrack(path,index):
            if index == len(digits):
                ans.append(path[:])
                return
            
            for l in letters[digits[index]]:
                backtrack(path+l, index+1)
        
        if digits:
            backtrack("",0)
            
        return ans