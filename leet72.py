#!/usr/bin/env python3
#-*- coding : utf-8-*-

def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    if not m or not n:
        return max(m, n)
    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for j in range(n + 1):
        memo[0][j] = j
    for i in range(m + 1):
        memo[i][0] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1]
            else:
                memo[i][j] = 1 + min(memo[i - 1][j - 1],
                                        memo[i - 1][j],
                                        memo[i][j - 1])
    return memo[-1][-1]
    
def t(word1, word2, ans):
    print(min_distance(word1, word2))
    print(ans)
    print()
    
    
if __name__ == '__main__':
    t('horse', 'ros', 3)
    t('intention', 'execution', 5)
    t('a', 'b', 1)