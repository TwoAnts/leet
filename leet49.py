#!/usr/bin/env python3
#-*- coding : utf-8-*-

def group_anagrams(strs):
    def str_id(s):
        arr = [0 for _ in range(26)]
        for c in s:
            arr[ord(c) - ord('a')] += 1
        return '#'.join((str(n) for n in arr))
    import collections
    ans = collections.defaultdict(list)
    for s in strs:
        ans[str_id(s)].append(s)
    return list(ans.values())

def t(strs, ans):
    print(group_anagrams(strs))
    print(ans)
    print()
    
    
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans = [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]
    t(strs, ans)