#!/usr/bin/env python3
#-*- coding : utf-8 -*-

def solve(a, b):
    l1, l2 = len(a), len(b)
    left = (l1 + l2) // 2
    extra = (l1 + l2 + 1) & 1
    num = left 
    if extra == 1:
        num -= 1
    i = 0
    j = 0
    while i < l1 and j < l2 and i + j < num:
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
        
    if i >= l1:
        j = num - i
        if extra == 1:
            return (b[j] + b[j + 1]) / 2
        return b[j]
    
    if j >= l2:
        i = num - j
        if extra == 1:
            return (a[i] + a[i + 1]) / 2
        return a[i]
    
    if extra:
        if a[i] < b[j]:
            if i + 1 < l1:
                return (a[i] + min(b[j], a[i+1])) /2
            return (a[i] + b[j]) / 2
        else:
            if j + 1 < l2:
                return (b[j] + min(b[j+1], a[i])) /2
        return (a[i] + b[j]) /2
    return min(a[i], b[j])
    


if __name__ == '__main__':
    a = [1, 3]
    b = [2]
    
    print(solve(a, b))
    
    a = [1, 2]
    b = [3, 4]
    
    print(solve(a, b))
    
    a = [1, 2]
    b = [-1, 3]
    
    print(solve(a, b))