class WordDictionary:

    def __init__(self):
        self.tries = {}

    def addWord(self, word: str) -> None:
        d = self.tries
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.tries
        def dfs(i, d):
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for k in d:
                        if k != '.' and dfs(j+1, d[k]):
                            return True
                    return False
                if c not in d:
                    return False
                d = d[c]
            return '.' in d
        
        return dfs(0, d)