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
    
def remove_nth_from_end(head, n):
    first_node = head
    for _ in range(n):
        if first_node is None:
            raise Exception('n is two large!')
        first_node = first_node.next
    if first_node is None:
        tmp = head.next
        head.next = None
        return tmp
    pre_node = head
    while first_node.next:
        pre_node = pre_node.next
        first_node = first_node.next
    tmp = pre_node.next
    assert(pre_node.next is not None)
    pre_node.next = pre_node.next.next
    tmp.next = None
    return head

def t(head, n, ans):
    print_list(remove_nth_from_end(head, n))
    print_list(ans)
    print()


if __name__ == '__main__':
    head = list_from_arr([1, 2, 3, 4, 5])
    t(head, 2, list_from_arr([1,2,3,5]))
    head = list_from_arr([1])
    t(head, 1, list_from_arr([]))
    