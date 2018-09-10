#!/usr/bin/env python3
#-*- coding : utf-8-*-

def gen_p(n):
    def gen_p_core(n, l_cnt, str_arr, res):
        if n == 0:
            for _ in range(l_cnt):
                str_arr.append(')')
            res.append(''.join(str_arr))
            for _ in range(l_cnt):
                str_arr.pop()
            return
        str_arr.append('(')
        gen_p_core(n - 1, l_cnt + 1, str_arr, res)
        str_arr.pop()
        if l_cnt > 0:
            str_arr.append(')')
            gen_p_core(n, l_cnt - 1, str_arr, res)
            str_arr.pop()
    
    str_arr = []
    res = []
    gen_p_core(n, 0, str_arr, res)
    return res

def t(n, ans):
    print(gen_p(n))
    print(ans)
    print()


if __name__ == '__main__':
    ans = [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
    t(3, ans)
    t(0, [''])
    t(1, ['()'])
    t(2, ['()()', '(())'])