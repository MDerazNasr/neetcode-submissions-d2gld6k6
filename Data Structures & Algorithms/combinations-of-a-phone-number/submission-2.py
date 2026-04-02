class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        1. handle base case
        2. implement recursivity
        3. remove changes
        '''
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
        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append(path)
                return
            for l in letters[digits[index]]:
                backtrack(index + 1, path + l)
        if digits:
            backtrack(0, "")
        return res


           