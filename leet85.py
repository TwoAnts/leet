#!/usr/bin/env python3
#-*- coding : utf-8-*-

def maximal_rectangle(matrix):
    max_area = 0
    def expand_max(matrix, x, y, h, w):
        nonlocal max_area
        w_expand = (w >= h) and x + w < len(matrix[0])
        if w_expand:
            for yi in range(y, y + h):
                if matrix[yi][x+w] == '0':
                    w_expand = False
                    break
            
        h_expand = (h >= w) and y + h < len(matrix)
        if h_expand:
            for xi in range(x, x + w):
                if matrix[y+h][xi] == '0':
                    h_expand = False
                    break
        #print(y, x, h_expand, w_expand)
        if w_expand and h_expand and matrix[y+h][x+w] == '1':
            #print(y, x, h + 1, w + 1)
            max_area = max(max_area, (h + 1) * (w + 1))
            expand_max(matrix, x, y, h + 1, w + 1)
        else:
            if w_expand:
                #print(y, x, h, w + 1)
                max_area = max(max_area, h * (w + 1))
            if h_expand:
                #print(y, x, h + 1, w)
                max_area = max(max_area, (h + 1) * w)
        if w_expand:
            expand_max(matrix, x, y, h, w + 1)
        if h_expand:
            expand_max(matrix, x, y, h + 1, w)
    
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == '1':
                max_area = max(max_area, 1)
                expand_max(matrix, x, y, 1, 1)
    return max_area

def t(matrix, ans):
    print(maximal_rectangle(matrix))
    print(ans)
    print()
    
if __name__ == '__main__':
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    t(matrix, 6)
    matrix = [
        ['1', '1'],
        ['1', '1']
    ]
    t(matrix, 4)
    matrix = [['1', '1']]
    t(matrix, 2)