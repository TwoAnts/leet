#!/usr/bin/env python3
#-*- coding : utf-8-*-
'''
def min_window(s, t):
    t = ''.join(sorted(t))
    indexes = [-1 for _ in t]
    def min_pos(i_arr):
        r = 0
        for i, index in enumerate(i_arr):
            if index < i_arr[r]:
                r = i
        return r
    min_window = None
    while True:
        c = min_pos(indexes)
        first_c = t.find(t[c])
        i = max(indexes[first_c:first_c + t.count(t[c])]) + 1
        while i < len(s):
            if s[i] == t[c]:
                indexes[c] = i
                break
            i += 1
        if i == len(s):
            break
        min_i = min(indexes)
        if min_i == -1:
            continue
        max_i = max(indexes)
        cur_len = max_i - min_i
        if (min_window is None 
            or (min_window[1] - min_window[0]) > cur_len):
            min_window = (min_i, max_i)
    if min_window is None:
        return ''
    return s[min_window[0]:min_window[1] + 1]
'''

def min_window(s, t):
    from collections import Counter
    need, missing = Counter(t), len(t)
    l = 0
    min_window = None
    for r, c in enumerate(s, 0):
        if c not in need:
            continue
        if need[c] > 0:
            missing -= 1
        need[c] -= 1
        if not missing:
            while l < r:
                if s[l] not in need:
                    l += 1
                    continue
                if need[s[l]] >= 0:
                    break
                need[s[l]] += 1
                l += 1
            if (min_window is None
                or min_window[1] - min_window[0] > r - l):
                min_window = (l, r)
            need[s[l]] += 1
            missing += 1
            l += 1
    if min_window is None:
        return ''
    return s[min_window[0]:min_window[1]+1]

def t(s, t, ans):
    print(min_window(s, t))
    print(ans)
    print()
    
if __name__ == '__main__':
    t("ADOBECODEBANC", "ABC", "BANC")
    t("ACCACBCACB", "ABB", "BCACB")