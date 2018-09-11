#!/usr/bin/env python3
#-*- coding : utf-8-*-

def print_matrix(m):
    for row in m:
        print(row)
    print()

def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

def t(m, ans):
    rotate(m)
    print_matrix(m)
    print_matrix(ans)
    print()
    
    
if __name__ == '__main__':
    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    ans = [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
    t(m, ans)
    
    m = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    ans = [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
    ]
    t(m, ans)