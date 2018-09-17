#!/usr/bin/env python3
#-*- coding : utf-8-*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def cycle_list_from_arr(arr, tail_index=0):
    if not arr:
        return None
    head = ListNode(arr[0])
    cycle_node = head if tail_index >= 0 else None
    head.next  = None
    it = head
    cnt = tail_index
    for value in arr[1:]:
        it.next = ListNode(value)
        it = it.next
        if cnt > 0:
            cnt -= 1
            if cnt == 0:
                cycle_node = it
    it.next = cycle_node
    return head
        
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
    
def detect_cycle(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            entry = head
            while entry is not slow:
                entry = entry.next
                slow = slow.next
            return entry
    return None
    
def t(head, ans):
    cycle_node = detect_cycle(head)
    print(cycle_node.val if cycle_node else None)
    print(ans)
    print()


if __name__ == '__main__':
    t(cycle_list_from_arr([1,2,3,4,5], 2), 3)
    t(cycle_list_from_arr([1,2,3,4,5], 0), 1)
    t(cycle_list_from_arr([1,2,3,4,5], -1), None)
    t(cycle_list_from_arr([1,2,3,4,5], 4), 5)
    