#!/usr/bin/env python3
#-*- coding : utf-8 -*-

def convert(s, numRows):
    if numRows == 1:
        return s
    r_arr = []
    l = len(s)
    step_sum = (numRows - 1) * 2
    for i in range(numRows):
        j = i
        step = step_sum - 2*i
        if step == 0:
            step = step_sum
        if step == step_sum:
            while j < l:
                r_arr.append(s[j])
                j += step
        else:
            while j < l:
                r_arr.append(s[j])
                j += step
                step = step_sum - step
    return ''.join(r_arr)

def t(s, n, ans):
    print(convert(s, n))
    print(ans)

if __name__ == '__main__':
    t('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')
    
    t('PAYPALISHIRING', 4, 'PINALSIGYAHRPI')
    
    t('A', 1, 'A')
    
    t('ABCD', 2, 'ACBD')