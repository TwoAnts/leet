#!/usr/bin/env python3
#-*- coding : utf-8-*-

def exist(board, word):
    if not board or not word:
        return False
    def core(board, word, i, x, y):
        if i == len(word):
            return True
        if (x < 0 or x >= len(board)
            or y < 0 or y >= len(board[0])):
            return False
        if board[x][y] != word[i]:
            return False
        tmp = board[x][y]
        board[x][y] = ''
        result = (
            core(board, word, i + 1, x - 1, y)
            or core(board, word, i + 1, x, y - 1)
            or core(board, word, i + 1, x + 1, y)
            or core(board, word, i + 1, x, y + 1)
        )
        board[x][y] = tmp
        return result
    for x in range(len(board)):
        for y in range(len(board[0])):
            if (board[x][y] == word[0]
                and core(board, word, 0, x, y)):
                return True
    return False

def t(board, word, ans):
    print(exist(board, word))
    print(ans)
    print()
    
if __name__ == '__main__':
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    t(board, 'ABCCED', True)
    t(board, 'SEE', True)
    t(board, 'ABCB', False)

    