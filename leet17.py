#!/usr/bin/env python3
#-*- coding : utf-8-*-

def solve(digits):
    def d2l(d):
        MAP = [
                   'abc', 'def',
            'ghi', 'jkl', 'mno',
            'pqrs', 'tuv', 'wxyz'
        ]
        n = int(d)
        if n - 2 < 0 or n - 2 >= len(MAP):
            return None
        return MAP[n - 2]
    def core(digits, i, str_arr, res):
        if i == len(digits):
            return res.append(''.join(str_arr))
        letters = d2l(digits[i])
        for c in letters:
            str_arr.append(c)
            core(digits, i + 1, str_arr, res)
            str_arr.pop()
    res = []
    str_arr = []
    if not digits:
        return res
    core(digits, 0, str_arr, res)
    return res

def t(digits, ans):
    print(solve(digits))
    print(ans)
    print()


if __name__ == '__main__':
    t("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    t("", [])