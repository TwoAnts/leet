#!/usr/bin/env python3
#-*- coding : utf-8-*-
    
def search(nums, target):
    def search_left_bound(nums, target, l, r):
        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            elif mid - 1 >= 0 and nums[mid - 1] == target:
                r = mid - 1
            else:
                return mid
        return -1
        
    def search_right_bound(nums, target, l, r):
        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            elif mid + 1 < len(nums) and nums[mid + 1] == target:
                l = mid + 1
            else:
                return mid
        return -1
    
    left = search_left_bound(nums, target, 0, len(nums) - 1)
    if left == -1:
        return [-1, -1]
    right = search_right_bound(nums, target, left, len(nums) - 1)
    return [left, right]

def t(nums, target, ans):
    print(search(nums, target))
    print(ans)
    print()


if __name__ == '__main__':
    t([5,7,7,8,8,10], 8, [3,4])
    t([5,7,7,8,8,10], 6, [-1,-1])