#!/usr/bin/env python3
#-*- coding : utf-8-*-

def is_valid(s):
    stack = []
    valid_pair = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for c in s:
        if c in ('(', '[', '{'):
            stack.append(c)
        elif not stack or valid_pair[c] != stack[-1]:
            return False
        else:
            stack.pop()
    
    return not stack

def t(s, ans):
    print(is_valid(s))
    print(ans)
    print()


if __name__ == '__main__':
    t('()', True)
    t('()[]{}', True)
    t('(]', False)
    t('([)]', False)
    t('{[]}', True)
    t('', True)