#!/usr/bin/env python3
#-*- coding : utf-8-*-

def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target < nums[mid]:
            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                if target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
        elif target > nums[mid]:
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                if target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        else:
            return mid
    return -1

def t(nums, target, ans):
    print(search(nums, target))
    print(ans)
    print()


if __name__ == '__main__':
    t([4,5,6,7,0,1,2], 0, 4)
    t([4,5,6,7,0,1,2], 9, -1)
    t([0,1,2], 1, 1)
    t([0,2], 2, 1)