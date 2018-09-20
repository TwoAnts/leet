#!/usr/bin/env python3
#-*- coding : utf-8-*-
'''
def subsets(nums):
    def core(nums, i, n_arr, res):
        if i == len(nums):
            res.append(n_arr[:])
            return
        core(nums, i+1, n_arr, res)
        n_arr.append(nums[i])
        core(nums, i+1, n_arr, res)
        n_arr.pop()
    n_arr = []
    res = []
    core(nums, 0, n_arr, res)
    return res
'''

def subsets(nums):
    res = [[]]
    for n in nums:
        res_len = len(res)
        for i in range(res_len):
            tmp = res[i][:]
            tmp.append(n)
            res.append(tmp)
    return res
    
def t(nums):
    print(subsets(nums))
    
if __name__ == '__main__':
    t([1,2,3])