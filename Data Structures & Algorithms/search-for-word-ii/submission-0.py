class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            d = trie
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['.'] = word
        
        res = []
        ROWS, COLS = len(board), len(board[0])
        def dfs(d, r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] not in d:
                return

            ch = board[r][c]
            d = d[ch]

            if '.' in d:
                res.append(d['.'])
                del d['.']
            
            board[r][c] = '#'
            dfs(d, r+1, c)
            dfs(d, r-1, c)
            dfs(d, r, c+1)
            dfs(d, r, c-1)
            board[r][c] = ch
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(trie, r, c)
        
        return res