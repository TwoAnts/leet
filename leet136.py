#!/usr/bin/env python3
#-*- coding : utf-8 -*-

def single_number(nums):
    num = 0
    for n in nums:
        num ^= n
    return num
    
def t(nums, ans):
    print(single_number(nums))
    print(ans)
    print()
    
    
if __name__ == '__main__':
    t([2,2,1], 1)
    t([4,1,2,1,2], 4)