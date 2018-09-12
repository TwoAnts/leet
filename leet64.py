#!/usr/bin/env python3
#-*- coding : utf-8-*-

def min_path_sum(grid):
    for col in range(1, len(grid[0])):
        grid[0][col] += grid[0][col - 1]
    for row in range(1, len(grid)):
        grid[row][0] += grid[row - 1][0]
    for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])
    return grid[-1][-1]

def t(grid, ans):
    print(min_path_sum(grid))
    print(ans)
    print()
    
if __name__ == '__main__':
    g = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    t(g, 7)
    g = [
        [1, 1],
        [2, 1]
    ]
    t(g, 3)