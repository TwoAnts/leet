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
    
def inter_lists_from_arr(arr1, arr2, arr3):
    headC = list_from_arr(arr3)
    headA = list_from_arr(arr1)
    headB = list_from_arr(arr2)
    it = headA
    while it.next:
        it = it.next
    it.next = headC
    it = headB
    while it.next:
        it = it.next
    it.next = headC
    return headA, headB

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
    
def get_intersection_node(headA, headB):
    lA = list_len(headA)
    lB = list_len(headB)
    it_long = headA
    it_short = headB
    ahead_step = lA - lB
    if lA < lB:
        it_long =  headB
        it_short = headA
        ahead_step = lB - lA
    while it_long and ahead_step > 0:
        it_long = it_long.next
        ahead_step -= 1
    
    while it_long is not it_short:
        it_long = it_long.next
        it_short = it_short.next
    return it_short

def t(headA, headB, ans):
    node = get_intersection_node(headA, headB)
    print(node.val if node else None)
    print(ans)
    print()
    
if __name__ == '__main__':
    t(*inter_lists_from_arr([1, 2], [3, 4, 5], [7, 8, 9]), 7)
    t(*inter_lists_from_arr([1, 2], [3, 4, 5], None), None)
    t(*inter_lists_from_arr([1, 2], [3, 4], [7, 8, 9]), 7)
    