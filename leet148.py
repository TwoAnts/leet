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
    
def list_len(head):
    it = head
    cnt = 0
    while it:
        it = it.next
        cnt += 1
    return cnt
        
def merge_list(head, step):
    """
    step: the length of sublist to merge
    return value: head, tail node of the merged list
    """
    if not head:
        return head, None
    new_head = ListNode(None)
    it = new_head
    #find the head2 
    it1 = head
    l1 = step
    while l1 > 0 and it1:
        it1 = it1.next
        l1 -= 1
    if not it1: # the second list is None
        return head, None
    #find the tail.next
    it2 = it1
    l2 = step
    while l2 > 0 and it2:
        l2 -= 1
        it2 = it2.next
    tail_next = it2
    
    #merge two sublist.
    it2 = it1
    it1 = head
    l1 = l2 = step
    while l1 > 0 and l2 > 0 and it1 and it2:
        if it1.val <= it2.val:
            it.next = it1
            it1 = it1.next
            l1 -= 1
        else:
            it.next = it2
            it2 = it2.next
            l2 -= 1
        it = it.next
    while l1 > 0 and it1:
        it.next = it1
        it = it.next
        it1 = it1.next
        l1 -= 1
    while l2 > 0 and it2:
        it.next = it2
        it = it.next
        it2 = it2.next
        l2 -= 1
    it.next = tail_next
    return new_head.next, it
    
def sort_list(head):
    k = 1
    new_head = ListNode(None)
    new_head.next = head
    l = list_len(head)
    while k < l:
        it = new_head
        head_it = new_head
        while it and it.next:
            head_it.next, it = merge_list(it.next, k)
            head_it = it
        k *= 2
    return new_head.next
    
def t(head, ans):
    print_list(sort_list(head))
    print_list(ans)
    print()
    
if __name__ == '__main__':
    t(list_from_arr([4, 2, 1, 3]), list_from_arr([1, 2, 3, 4]))
    t(list_from_arr([-1, 5, 3, 4, 0]), list_from_arr([-1, 0, 3, 4, 5]))