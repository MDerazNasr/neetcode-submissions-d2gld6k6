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

'''
 "So the brute force would be to take each word and search the entire board for it, but that's way too
   slow if we have a lot of words. Instead, we flip it — we build a trie from all the words, then walk
  the board once and let the trie tell us which paths are worth exploring.

  Building the trie:

  We insert every word into a nested dict. Each level represents one character. At the end of a word,
  we store the full word under '.' — that way when we find a match during the board search, we can just
   grab it directly without tracking what characters we've seen.

  Searching the board:

  We try starting a DFS from every cell on the board. At each cell, we check if the current character
  exists in our current trie node. If it doesn't, no word in our list can be formed down this path, so
  we prune — this is where the trie saves us time.

  If the character does exist, we move deeper into both the board and the trie. If we land on a node
  that has '.', that means we've completed a word — we add it to our result and delete the marker so we
   don't add it again.

  To avoid using the same cell twice in one path, we temporarily replace the cell with '#' before
  exploring neighbors, then restore it after — standard backtracking.

  Time complexity:

  Building the trie is O(total characters across all words). The board search is O(rows * cols * 4^L)
  in the worst case where L is the max word length, since from each cell we branch into 4 directions.
  But in practice the trie pruning cuts this down significantly.

  Space complexity:

  O(total characters) for the trie, plus O(L) for the recursion stack depth."

'''