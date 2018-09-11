#!/usr/bin/env python3
#-*- coding : utf-8-*-
    
def search_insert(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return mid
    return l

def t(nums, target, ans):
    print(search_insert(nums, target))
    print(ans)
    print()
    
if __name__ == '__main__':
    t([1,3,5,6], 2, 1)
    t([1,3,5,6], 7, 4)
    t([1,3,5,6], 5, 2)
    t([1,3,5,6], 0, 0)