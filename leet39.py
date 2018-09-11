#!/usr/bin/env python3
#-*- coding : utf-8-*-

def combine_sum(candidates, target):
    def core(index, cur_sum, num_arr, res):
        if cur_sum == target:
            res.append(num_arr[:])
            return
        if index >= len(candidates):
            return
        cnt = 0
        while cur_sum <= target:
            core(index + 1, cur_sum, num_arr, res)
            cur_sum += candidates[index]
            num_arr.append(candidates[index])
            cnt += 1
        while cnt > 0:
            num_arr.pop()
            cnt -= 1
    
    num_arr = []
    res = []
    core(0, 0, num_arr, res)
    return res
    
def t(candidates, target, ans):
    print(combine_sum(candidates, target))
    print(ans)
    print()
    
if __name__ == '__main__':
    t([2,3,6,7], 7, [[7], [2,2,3]])
    t([2,3,5], 8, [[2,2,2,2], [2,3,3], [3,5]])