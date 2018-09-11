#!/usr/bin/env python3
#-*- coding : utf-8-*-
'''
def trap(height):
    if not height:
        return 0
    l = 0
    r = len(height) - 1
    old_h = 0
    cur_h = 0
    water = 0
    while l < r:
        while l < r and height[l] <= cur_h:
            l += 1
        while l < r and height[r] <= cur_h:
            r -= 1
        old_h = cur_h
        cur_h = min(height[l], height[r])
        for i in range(l + 1, r):
            if height[i] < cur_h:
                water += min(cur_h - old_h, cur_h - height[i])
    return water
'''

def trap(height):
    l = 0
    r = len(height) - 1
    l_h_max = 0
    r_h_max = 0
    water = 0
    while l < r:
        l_h_max = max(l_h_max, height[l])
        r_h_max = max(r_h_max, height[r])
        if l_h_max < r_h_max:
            water += (l_h_max - height[l])
            l += 1
        else:
            water += (r_h_max - height[r])
            r -= 1
        
    return water

def t(height, ans):
    print(trap(height))
    print(ans)
    print()
    
if __name__ == '__main__':
    t([0,1,0,2,1,0,1,3,2,1,2,1], 6)
    t([0,1,0, 0, 1], 2)
    t([1, 2, 1, 4], 1)