#!/usr/bin/env python3
#-*- coding : utf-8-*-

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return '[%s, %s]' %(self.start, self.end)
        
def ifl(l):
    return [Interval(r[0], r[1]) for r in l]
    
def print_intrevals(intervals):
    print(','.join((str(interval) for interval in intervals)))

def merge(intervals):
    #the compare func is my idea, still have some problems.
    from functools import cmp_to_key
    def interval_compare(i1, i2):
        if i2.start > i1.end:
            return -1
        if i1.start > i2.end:
            return 1
        return 0
    intervals.sort(key=cmp_to_key(interval_compare))
    res = []
    for interval in intervals:
        res.append(interval)
        while len(res) > 1:
            a, b = res[-2], res[-1]
            if a.start <= b.end and b.start <= a.end:
                a.start = min(a.start, b.start)
                a.end = max(a.end, b.end)
                res.pop()
            else:
                break
    return res
    
def t(intervals, ans):
    print_intrevals(merge(intervals))
    print_intrevals(ans)
    print()
    
    
if __name__ == '__main__':
    t(ifl([[1,3],[2,6],[8,10],[15,18]]), ifl([[1,6],[8,10],[15,18]]))
    t(ifl([[1,4],[4,5]]), ifl([[1,5]]))
    t(ifl([[2,3],[4,5],[6,7],[8,9],[1,10]]), ifl([[1,10]]))
    
    