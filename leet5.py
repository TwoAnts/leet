#!/usr/bin/env python3
#-*- coding : utf-8 -*-

def extend_max(s, start, end):
    while start >= 0 and end < len(s) and s[start] == s[end]:
        start -= 1
        end += 1
    return end - start - 1, (start + 1, end - 1)

def par_max(s):
    max_len = 1
    max_sub = (0, 0)
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i+1]:
            max_tmp, sub_tmp = extend_max(s, i, i+1)
            if max_len < max_tmp:
                max_len = max_tmp
                max_sub = sub_tmp
        if i + 2 < len(s) and s[i] == s[i+2]:
            max_tmp, sub_tmp = extend_max(s, i, i+2)
            if max_len < max_tmp:
                max_len = max_tmp
                max_sub = sub_tmp
    return s[max_sub[0]:max_sub[1]+1]
    
def t(s):
    print(par_max(s))

if __name__ == '__main__':
   t('aba')
   
   t('aabbcc')
   
   t('aabbbbaa')
   
   t('abcdef')