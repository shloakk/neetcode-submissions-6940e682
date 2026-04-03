class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word_idx):
            print(i, j, word[word_idx], word_idx)
            if board[i][j] != word[word_idx]:
                return False
            
            if word_idx == len(word) - 1:
                return True

            tmp, board[i][j] = board[i][j], "#"

            found = (
                (i > 0 and dfs(i-1, j, word_idx+1)) or
                (i < len(board) - 1 and dfs(i+1, j, word_idx+1)) or
                (j > 0 and dfs(i, j-1, word_idx+1)) or
                (j < len(board[0]) - 1 and dfs(i, j+1, word_idx+1))
            )

            board[i][j] = tmp
            return found

        for i in range(len(board)):
            for j in range (len(board[0])):
                letter = board[i][j]
                if letter == word[0]:
                    print(i, j, letter)
                    if dfs(i, j, 0):
                        return True
        
        return False