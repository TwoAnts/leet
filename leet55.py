#!/usr/bin/env python3
#-*- coding : utf-8-*-

def can_jump(nums):
    i = len(nums) - 2
    last_index = i + 1
    while i >= 0:
        if nums[i] >= last_index - i:
            last_index = i
        i -= 1
        
    return last_index == 0

def t(nums, ans):
    print(can_jump(nums))
    print(ans)
    print()
    
    
if __name__ == '__main__':
    t([2,3,1,1,4], True)
    t([3,2,1,0,4], False)