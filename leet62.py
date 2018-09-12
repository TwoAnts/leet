#!/usr/bin/env python3
#-*- coding : utf-8-*-
'''
def unique_paths(m, n):
    from collections import deque
    memo = [[0 for _ in range(m)] for _ in range(n)]
    memo[0][0] = 1
    dq = deque([(0, 0)])
    while dq:
        pos = dq.popleft()
        if pos != (0, 0) and memo[pos[1]][pos[0]] > 0:
            continue
        if 0 <= pos[0] - 1:
            memo[pos[1]][pos[0]] += memo[pos[1]][pos[0] - 1]
        if 0 <= pos[1] - 1:
            memo[pos[1]][pos[0]] += memo[pos[1] - 1][pos[0]]
        if pos[0] + 1 < m:
            dq.append((pos[0] + 1, pos[1]))
        if pos[1] + 1  < n:
            dq.append((pos[0], pos[1] + 1))
    return memo[-1][-1]
'''

def unique_paths(m, n):
    memo = [[1 for _ in range(m)] for _ in range(n)]
    for row in range(1, n):
        for col in range(1, m):
            memo[row][col] = memo[row - 1][col] + memo[row][col - 1]
    return memo[-1][-1]
    
def t(m, n, ans):
    print(unique_paths(m, n))
    print(ans)
    print()
    
    
if __name__ == '__main__':
    t(3, 2, 3)
    t(7, 3, 28)
    t(2, 2, 2)
    t(1, 1, 1)