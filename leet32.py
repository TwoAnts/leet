#!/usr/bin/env python3
#-*- coding : utf-8-*-
'''
#still wrong
def longest_p(s):
    if not s:
        return 0
    longest = 0
    l = 0
    r = 0
    last_r = r
    l_cnt = 0
    while l < len(s):
        first_l_cnt = 0
        while r < len(s):
            if s[r] == '(':
                if (first_l_cnt == 0
                    and r - 1 >= 0
                    and s[r - 1] == ')'):
                    first_l_cnt = l_cnt
                l_cnt += 1
            else:
                if l_cnt > 0:
                    l_cnt -= 1
                    if l_cnt == 0:
                        last_r = r
                        first_l_cnt = 0
                else:
                    break
            r += 1
        if last_r > l:
            longest = max(longest, last_r - l + 1)
        if first_l_cnt > 0:
            last_r += first_l_cnt
        else: 
            last_r += 1
        l = last_r
        r = l
        l_cnt = 0

    return longest
'''

'''
def longest_p(s):
    if not s:
        return 0
    dp = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        if s[i] == ')':
            if s[i - 1] == '(':
                dp[i] = 2
            elif i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == '(':
                dp[i] = 2 + dp[i - 1]
            else: 
                continue
            if i - dp[i] >= 0 and dp[i - dp[i]] > 0:
                dp[i] += dp[i - dp[i]]
    return max(dp)
'''
def longest_p(s):
    if not s:
        return 0
    longest = 0
    stack = [-1]
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if stack:
                    longest = max(longest, i - stack[-1])
            if not stack:
                stack.append(i)
    return longest
 
def t(s, ans):
    print(longest_p(s))
    print(ans)
    print()
    
    
if __name__ == '__main__':
    t('(()', 2)
    t(')()())', 4)
    t('((())', 4)
    t('', 0)
    t('(', 0)
    t(')', 0)
    t('((()())())', 10)
    t("(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()())))(())()())((((()())((())))((()))()())))()(()()()(()((()))()()()))()()()(()()((((())()(((()(((())((()))()((()(()))()())))))))))())()())(()()))((()()()()())))((()()((((()()))))(())())()()))))(())()(()))((((((()))(()()()()(())(()((()))(()(())(((()()))(()((((()((((()((((())(())))()(())))()))(()((((((((())()()((())((()())()))))())())()(((((()()(((((())()((()(((()))(()(()))(()(()())))())(()((((()((()(((((()()))((()(()((())()))))(()(()())((()((()((((())))(()())()))()())())()))))(())))(())()((())(()(()))))()())(((()(()(((((((((()(()()())))((()((()())())())(((((()(()))))()))()))))()())()(()(())))(()))))(()))(((()))))())))))(((())((())((((()((()))((())))()))(((()))())()))()()()((()()(()())(()))()()((()())))))())(()())(((())))))())(())()))()())())(()(()((())((()(()((())(()()()(()((()(((()(())()(((())))))()())))))(()((((()(()()))(((())(()))(()()))))(())()((()))()))()()))()((())(()())())())(()))(()()(())()(()((((()())(((())(()()())())(()()))())))(()((())(()()))))(()))((()()((((()())(()()))()())()())))()(()((((())())()(())()))()()(()(()))))))(((()()((()))(()((((()()((())))())())))()())))())))((())()()()))()((()((()))()()())))(())())(()(()(()(()))())()))(())((())()())(((()()(((())(()()))(()())(())))()))(((()()()())))())))(((()))())())())))(((()))()())())())))))()()()()(())))(()())))(()()())))()((((()()()((((()))()())))(()))()))))(()())()))(((((())()((())()))(()())()()()())()(((()(()(())))))(()(((()()))((((()()))()))(((())(()(()))()(())))()()(()))))()))))()())))()))((((((((()()())((()(()()()(((())())())))()()(())(())))()())()())))((()))((((())()()))(())(((())(()()(((((()()((()()(((()(()()(((())()))))()(()())(()((((()()())(((()))(())((())()))))())))))(()()()())))()))(())((()())()())()()))(())))((()))()()((()())()()))(()()(())()())(())))((()(((())))()))))((((()))((())())())()(())(()))((((((())()()(((((()))()())(((()(()(())()((()())))(((())(()(())))))(()(()(((()))(())((((())))((())((((((((()(((((()(())))((((((())(()((((()(())()()((())())())((((((((()))))(((())()))()()))(())(())()()())(()()((())(()))())(((())(()((())(())(())))))(()(()(()()(((()()()))())(()))(())())()(((()((())((()())()(((((()()(()))))(((())()()))(()(()(()(()((())))))))(())())()))()(()(()))))()()((((())()())(((())(()))((()())(()((())()()(())((((())))))(())())())(())(()()(()()))(((()((((())(((())))))(()()()()(((()((((())(()))((())()))()(((((((()(()())))((()()(()()((())()))()(())))((()()((((()()()))((())()))((())(((()(()()()(((()((())((())()())())))((()))))))))))(())()()(((()()())))(((()))(()))))(((()(()())(()))(())((()))(((()(()()(((((((()())((((()))((((()(()())())()(((()(()((()))))))))))()()(((()()((((((((((())))))((((())())((()(((()())()))()()(((((())(()())())(((()((())((((((())(((())(((()(()(((((((()(())()())(()))))(()(((()))))))()))(((())))(()(()())()))(()()(()(()((()())()(())((()()((()()()(()(()()))(((((())()(()())()((()())()))(((((()((())()((()((((()(((())())(()()(())()(())(()(())))))(()())((()((()()()())(()))(()))))))(()((())(())((())()())()()))(()((()))(()()))()())(())(()()(()))((())()((())((((((())()(()()(((((())(()())())())()()(()())))))()))()((())((((((()())((()))))))((()(()()(((((((())))))))((()))(())(((()(()(())()()()()(()(())()))))))())()))()(((((()(())(((()))((()))()))()()(()(()((())(()))))()())((()())))))))(()()(()()))()((()(())()((())(()()))())((()())())()()))))((((()()()))())(())()())))()))()))))()))((()(()())()))()))(((()()()()())))())()))((()()())((()())))(((()((()()())(())))()(())(()(()(())(()(((((()()()(((())()())(()((()())(()(((()(())((((()())()(())))(((((((()))))())())))(()))()()(((()())(()))()())(())()))()((())()((())((()((())()())(()()))(((((()()()((((((((()(()((()()((((((()())))((((((())))())(()(()((((()(()())())()()))()((())())(()((((()(((()())((())))))(()())(()()()(()))()())()()))((()((()())(())()()()((())()()))))())()))())))(()))(()))()))((())()((()((()))))))())(((()))))))()(((()((())))((()())())()))((()(()(()(()))((()()))())))(()())))())(()))(())(())))))()(())(()()))()))((())))(()))(()))))(())()())(()(()))())(()(())(())))(()))())(()())))())(()())((()))()()((()(()()()(((((()((()((())(()())(())))()))))))(((())())))()((((()))()((()))())()))()))(()(()((()()())()()(((()))())))))()((((()()))))()))())))()())))(((((()(())))())(((()))((()))(((()(())())()((()(((()))()())))))((((()))()(()((((((()(()()()())(())((()))()(()()))))))()(((())))(())()())))))((()))(())()))))(()(((()()((())(()))))(((((()))))())))()(())(()(()))()))()))(()((())(()((()())()(((()))))())(())()(())))((())(()(((()))(((((()))(()))())))(()((((((())()((((())())()))((())))))())(()(())())))))()()(((())()())))))()))()())))()(())())(())()()()(((())))(())(((()))(()(((()()))())((()))(((()()()()())()()))(()))))()()))))(((()()))))()()(()()))()()()())())()((())(((()())(((())(()((()(((()(()())()()()(()((())(()()(()()()))))))()((()))))()(()))()))(())()()())))()()(((()))((()()(((()())))((()()())((())))))()())()((())))())(()())()()()()((())((()()())((()()))())(())())()(()(((()))())(()))))(()()))(())))))))()())()((()())()()))()())))((()()(()())()(()))((())()))(((())))())))(((()()())())(", 2684)
    