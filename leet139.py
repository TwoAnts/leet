#!/usr/bin/env python3
#-*- coding : utf-8 -*-
'''
def word_break(s, wordDict):
    wordDict = set(wordDict)
    dp = [None for _ in range(len(s))]
    def core(s, wordDict, start, dp):
        if dp[start] is not None:
            return dp[start]
        if s[start:] in wordDict:
            dp[start] = True
            return True
        for i in range(start, len(s) - 1):
            if (s[start:i+1] in wordDict
                and core(s, wordDict, i+1, dp)):
                dp[start] = True
                return True
        dp[start] = False
        return False
    
    return core(s, wordDict, 0, dp)
'''
def word_break(s, wordDict):
    dp = [False for _ in range(len(s))]
    len_set = set((len(word) for word in wordDict))
    wordDict = set(wordDict)
    for i in range(len(s)):
        for j in len_set:
            if (i+1 >= j 
                and s[i+1-j:i+1] in wordDict 
                and (i - j == -1 or dp[i-j])):
                dp[i] = True
    return dp[-1]
    
def t(s, wordDict, ans):
    print(word_break(s, wordDict))
    print(ans)
    print()
    
    
if __name__ == '__main__':
    t('leetcode', ['leet', 'code'], True)
    t('applepenapple', ["apple", "pen"], True)
    t('catsandog', ["cats", "dog", "sand", "and", "cat"], False)