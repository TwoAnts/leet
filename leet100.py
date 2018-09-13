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
    
def tree_to_iter(root):
    from collections import deque
    if not root:
        return
    queue = deque()
    queue.append(root)
    yield root.val
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
            yield node.left.val
        else:
            yield None
        if node.right:
            queue.append(node.right)
            yield node.right.val
        else:
            yield None
        
def is_same_tree(p, q):
    iter_p = tree_to_iter(p)
    iter_q = tree_to_iter(q)
    while True:
        p_val = next(iter_p, '#')
        q_val = next(iter_q, '#')
        if (p_val == '#' 
            or q_val == '#'
            or p_val != q_val):
            break
    return p_val == q_val
    
def t(p, q, ans):
    print(is_same_tree(p, q))
    print(ans)
    print()
    
if __name__ == '__main__':
    t(tree_from_list([2, 1, 3]), tree_from_list([2, 1, 3]), True)
    t(tree_from_list([1, 2]), tree_from_list([1, None, 2]), False)
    t(tree_from_list([1, 2, 1]), tree_from_list([1, 1, 2]), False)