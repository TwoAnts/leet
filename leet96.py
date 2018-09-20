#!/usr/bin/env python3
#-*- coding : utf-8-*-

        
def num_trees(n):
    g = [0 for _ in range(n + 1)]
    g[0] = 1 
    g[1] = 1 
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            g[i] += g[j - 1] * g[i - j]
    return g[n]
    
def t(n, ans):
    print(num_trees(n))
    print(ans)
    print()
    
if __name__ == '__main__':
    t(3, 5)