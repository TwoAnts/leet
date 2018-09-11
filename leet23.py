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
    
def merge_k_list(lists):
    from heapq import heapify, heapreplace, heappop
    choices = []
    new_head = ListNode(0)
    it = new_head
    for i, node in enumerate(lists):
        if node is not None:
            choices.append((node.val, i))
    heapify(choices)
    while choices:
        val, list_index = choices[0]
        cur_list = lists[list_index]
        it.next = cur_list
        it = it.next
        lists[list_index] = cur_list.next
        if cur_list.next is not None:
            heapreplace(choices, (cur_list.next.val, list_index))
        else:
            heappop(choices)
    it.next = None
    return new_head.next
    
def t(lists, ans):
    print_list(merge_k_list(lists))
    print_list(ans)
    print()


if __name__ == '__main__':
    t([list_from_arr([1, 4, 5]), list_from_arr([1, 3, 4]), list_from_arr([2, 6])], list_from_arr([1, 1, 2, 3, 4, 4, 5, 6]))
    t([list_from_arr([1]), list_from_arr([2])], list_from_arr([1, 2]))
    t([list_from_arr([]), list_from_arr([])], list_from_arr([]))