#!/usr/bin/env python3
#-*- coding : utf-8-*-

def premute(nums):
    def core(nums, index, res):
        if index >= len(nums) - 1:
            res.append(nums[:])
            return 
        core(nums, index + 1, res)
        for i in range(index + 1, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            core(nums, index + 1, res)
            nums[index], nums[i] = nums[i], nums[index]
            
    res = []
    core(nums, 0, res)
    return res
    
def t(nums, ans):
    print(premute(nums))
    print(ans)
    print()
    
    
if __name__ == '__main__':
    t([1,2,3], None)