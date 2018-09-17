#!/usr/bin/env python3
#-*- coding : utf-8-*-

def longest_consecutive(nums):
    length = 0
    nums = set(nums)
    for n in nums:
        if n - 1 not in nums:
            i = 1
            while n + i in nums:
                i += 1
            length = max(length, i)
    return length

def t(nums, ans):
    print(longest_consecutive(nums))
    print(ans)
    print()
    
if __name__ == '__main__':
    t([100, 4, 200, 1, 3, 2], 4)