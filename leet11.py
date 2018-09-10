#!/usr/bin/env python3
#-*- coding : utf-8-*-
'''
def max_area(height):
    pos_array = [(h, i) for i, h in enumerate(height)]
    pos_array.sort(key = lambda e : e[0], reverse=True)
    #rint(pos_array)
    max_tmp = 0
    for i in range(1, len(pos_array)):
        max_range = 0
        for j in range(i):
            h1, b1 = pos_array[i]
            h2, b2 = pos_array[j]
            if abs(b1 - b2) <= max_range:
                continue
            max_range = abs(b1 - b2)
            area = h1 * max_range
            if area > max_tmp:
                max_tmp = area
    return max_tmp
'''
'''
def max_area(height):
    l = 0
    r = 1
    max_tmp = 0
    max_l = 0
    old_max_l = 0
    while r < len(height):
        while r + 1 < len(height) and height[r] <= height[r + 1]:
            r += 1
        if height[max_l] < height[r - 1]:
            max_l = r - 1
        l = max_l
        #print(l, r, height[l], height[r])
        while l >= 0:
            area = (r - l) * min(height[l], height[r])
            if area > max_tmp:
                max_tmp = area
            l -= 1
        if height[max_l] < height[r]:
            max_l = r
        r += 1
    return max_tmp
'''
def max_area(height):
    l = 0
    r = len(height) - 1
    max_tmp = 0
    while l < r:
        max_tmp = max(max_tmp, (r - l) * min(height[l], height[r]))
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return max_tmp
    
def t(h, ans):
    print(max_area(h))
    print(ans)
    print()

if __name__ == '__main__':
    t([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
    t([1, 2, 1, 1], 3)
    t([1, 1], 1)
    t([5,2,12,1,5,3,4,11,9,4], 55)
    t([1,2,3,4,5,6,7,8,9,10], 25)
    t([2, 1, 1, 1, 10, 2], )