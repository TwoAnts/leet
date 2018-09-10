#!/usr/bin/env python3
#-*- coding : utf-8 -*-

def solve(s):
    max_len = 0 if not s else 1
    char_set = set()
    i = 0
    j = i + 1
    while i < len(s) - max_len:
        char_set.add(s[i])
        j = max(j, i + 1)
        while j < len(s):
            if s[j] in char_set:
                break
            else:
                char_set.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1
        
        i += 1
        char_set.remove(s[i - 1])
    
    return max_len


if __name__ == '__main__':
    s = 'abcabcbb'
    print(solve(s))
    
    s = 'bbbbb'
    print(solve(s))
    
    s = 'pwwkew'
    print(solve(s))
    
    s = 'au'
    print(solve(s))
    
    s = ' '
    print(solve(s))