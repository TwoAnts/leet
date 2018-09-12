#!/usr/bin/env python3
#-*- coding : utf-8-*-
'''
def sort_colors(nums):
    i = j = 0
    for k in range(len(nums)):
        tmp = nums[k]
        nums[k] = 2
        if tmp < 2:
            nums[j] = 1
            j += 1
        if tmp == 0:
            nums[i] = 0
            i += 1
'''
            
def sort_colors(nums):
    red, white, blue = 0, 0, len(nums) - 1
    while white <= blue:
        if nums[white] == 0:
            nums[white], nums[red] = nums[red], nums[white]
            white += 1
            red += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
        

def t(nums, ans):
    sort_colors(nums)
    print(nums)
    print(ans)
    print()
    
    
if __name__ == '__main__':
    t([2,0,2,1,1,0], [0,0,1,1,2,2])