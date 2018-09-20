#!/usr/bin/env python3
#-*- coding : utf-8-*-

def max_profit(prices):
    if not prices:
        return 0
    cur_min = prices[0]
    cur_max = prices[0]
    max_gain = 0
    for p in prices[1:]:
        if p > cur_max:
            cur_max = p
        elif p < cur_min:
            cur_min = p
            cur_max = p
        else:
            continue
        max_gain = max(max_gain, cur_max - cur_min)
    return max_gain
    
def t(prices, ans):
    print(max_profit(prices))
    print(ans)
    print()
    
if __name__ == '__main__':
    t([7,1,5,3,6,4], 5)
    t([7,6,4,3,1], 0)