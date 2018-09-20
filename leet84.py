#!/usr/bin/env python3
#-*- coding : utf-8-*-
'''
def largest_area(heights):
    sorted_heights = [(h, i) for i, h in enumerate(heights)]
    sorted_heights.sort()
    largest = 0
    for i, (h, real_index) in enumerate(sorted_heights):
        l = 0
        r = len(heights) - 1
        li = i
        while li >= 0 and sorted_heights[li][0] == sorted_heights[i][0]:
            li -= 1
        if li >= 0:
            for _, index in sorted_heights[:li + 1]:
                if l <= index < real_index:
                    l = index + 1
                if r >= index > real_index:
                    r = index - 1
        cur_area = (r - l + 1) * h
        #print(real_index, h, l, r)
        if cur_area > largest:
            largest = cur_area
    return largest
'''

def largest_area(heights):
    heights.append(0)
    stack = [-1]
    largest = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            cur_area = h * w
            largest = max(largest, cur_area)
        stack.append(i)
    heights.pop()
    return largest
    
def t(heights, ans):
    print(largest_area(heights))
    print(ans)
    print()
    
if __name__ == '__main__':
    t([2,1,5,6,2,3], 10)