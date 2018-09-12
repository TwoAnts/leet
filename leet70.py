#!/usr/bin/env python3
#-*- coding : utf-8-*-


def climb_stairs(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    n -= 2
    memo = [1, 2, 0]
    index = 1
    while n > 0:
        index = (index + 1) % 3 
        memo[index] = sum(memo) - memo[index]
        n -= 1
    return memo[index]

def t(n, ans):
    print(climb_stairs(n))
    print(ans)
    print()
    
    
if __name__ == '__main__':
    t(2, 2)
    t(3, 3)