#!/usr/bin/env python3
#-*- coding : utf-8-*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def tree_from_list(l):
    from collections import deque
    root = TreeNode(l[0])
    queue = deque()
    queue.append(root)
    i = 1
    while i < len(l):
        node = queue.popleft()
        if l[i]:
            node.left = TreeNode(l[i])
            queue.append(node.left)
        if i+1 < len(l) and l[i+1]:
            node.right = TreeNode(l[i + 1])
            queue.append(node.right)
        i += 2
    return root
    
def tree_to_list(root):
    l = []
    from collections import deque
    queue = deque()
    queue.append(root)
    l.append(root.val)
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
            l.append(node.left.val)
        else:
            l.append(None)
        if node.right:
            queue.append(node.right)
            l.append(node.right.val)
        else:
            l.append(None)
    while l and l[-1] is None:
        l.pop()
    return l
    
def max_path_sum(root):
    max_sum = root.val
    def core(root):
        if not root:
            return 0
        nonlocal max_sum
        l = core(root.left)
        r = core(root.right)
        cur_sum = root.val
        if l > 0:
            cur_sum += l
        if r > 0:
            cur_sum += r
        max_sum = max(cur_sum, max_sum)
        cur_ret = root.val
        if max(l, r) > 0:
            cur_ret += max(l, r)
        return cur_ret
    core(root)
    return max_sum
    
def t(root, ans):
    print(max_path_sum(root))
    print(ans)
    print()
    
if __name__ == '__main__':
    t(tree_from_list([1,2,3]), 6)
    t(tree_from_list([-10, 9, 20, None, None, 15, 7]), 42)
    t(tree_from_list([1, 2, 3, None, None, -4, -5]), 6)
    t(tree_from_list([1, 2, 3, None, None, -6, 2]), 8)