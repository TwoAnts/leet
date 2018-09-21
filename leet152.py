#!/usr/bin/env python3
#-*- coding : utf-8-*-
'''
def max_product(nums):
    if not nums:
        return None
    product_max = nums[0]
    cur_pos_max = None
    cur_neg_min = None
    for n in nums:
        if n == 0:
            cur_pos_max = 0
            cur_neg_min = 0
        elif n > 0:
            if (cur_pos_max is not None 
                and cur_pos_max != 0):
                cur_pos_max *= n
            else:
                cur_pos_max = n
            if cur_neg_min is not None:
                cur_neg_min *= n
        else:
            tmp = cur_neg_min
            cur_neg_min = n
            if cur_pos_max and cur_pos_max > 0:
                cur_neg_min = cur_pos_max * n
                
            if tmp and tmp < 0:
                cur_pos_max = tmp * n
            elif cur_pos_max and cur_pos_max > 0:
                cur_pos_max = None
                
        #print(n, cur_pos_max, cur_neg_min)
        if cur_pos_max is not None:
            product_max = max(product_max, cur_pos_max)
        if cur_neg_min is not None:
            product_max = max(product_max, cur_neg_min)
    return product_max
'''
def max_product(nums):
    if not nums:
        return None
    product_max = cur_max = cur_min = nums[0]
    for n in nums[1:]:
        cur_max, cur_min = (max(cur_max*n, cur_min*n, n),
                            min(cur_max*n, cur_min*n, n))
        product_max = max(product_max, cur_max)
    return product_max
    
def t(nums, ans):
    print(max_product(nums))
    print(ans)
    print()
    
if __name__ == '__main__':
    t([2, 3, -2, 4], 6)
    t([-2, 0, -1], 0)
    t([-2, 0, 0, -1], 0)
    t([0, 2], 2)
    t([-4, -3], 12)
    t([2, -5, -2, -4, 3], 24)