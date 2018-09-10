#!/usr/bin/env python3
#-*- coding : utf-8-*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def list_from_arr(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    head.next  = None
    it = head
    for value in arr[1:]:
        it.next = ListNode(value)
        it = it.next
    it.next = None
    return head

def print_list(node):
    if node is None:
        print('None')
        return
    it = node
    res = []
    while it:
        res.append(str(it.val))
        it = it.next
    print('->'.join(res))
    
def merge_list(l1, l2):
    new_head = ListNode(0)
    it = new_head
    it1, it2 = l1, l2
    while it1 and it2:
        if it1.val < it2.val:
            it.next = it1
            it1 = it1.next
        else:
            it.next = it2
            it2 = it2.next
        it = it.next
            
    while it1:
        it.next = it1
        it1 = it1.next
        it = it.next
    while it2:
        it.next = it2
        it2 = it2.next
        it = it.next
    
    it.next = None 
    return new_head.next
    
def t(l1, l2, ans):
    print_list(merge_list(l1, l2))
    print_list(ans)
    print()


if __name__ == '__main__':
    t(list_from_arr([1, 2, 4]), list_from_arr([1, 3, 4]), list_from_arr([1, 1, 2, 3, 4, 4]))
    t(list_from_arr([1]), list_from_arr([2]), list_from_arr([1, 2]))
    t(list_from_arr([]), list_from_arr([]), list_from_arr([]))