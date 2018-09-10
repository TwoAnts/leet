#!/usr/bin/env python3
#-*- coding:utf-8 -*-


def is_match_core(s, p, si, pi):
    if si == len(s):
        if pi + 1 < len(p) and p[pi + 1] == '*':
            if is_match_core(s, p, si, pi + 2):
                return True
        if pi == len(p):
            return True
        return False
    elif pi >= len(p):
        return False
    
    if pi + 1 < len(p) and p[pi + 1] == '*':
        if p[pi] == '.' or s[si] == p[pi]:
            return (is_match_core(s, p, si + 1, pi)
                    or is_match_core(s, p, si, pi + 2))
        else:
            return is_match_core(s, p, si, pi + 2)
    else:
        if p[pi] == '.' or s[si] == p[pi]:
            return is_match_core(s, p, si + 1, pi + 1)
        else:
            return False
    
    return False

def is_match(s, p):
    return is_match_core(s, p, 0, 0)

def t(s, p, ans):
    print(is_match(s, p))
    print(ans)
    print('')

if __name__ == '__main__':
    t('aa', 'a', False)
    t('aa', 'a*', True)
    t('ab', '.*', True)
    t('aab', 'c*a*b', True)
    t('aab', 'c*a*b*', True)
    t('', '', True)
    t('', 'c*c*', True)