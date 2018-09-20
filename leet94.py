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
        
def inorder_traverse(root):
    res = []
    stack = []
    it = root
    while it is not None:
        stack.append(it)
        it = it.left
    while stack:
        it = stack.pop()
        res.append(it.val)
        it = it.right
        while it is not None:
            stack.append(it)
            it = it.left
    return res
    
def t(tree, ans):
    print(inorder_traverse(tree))
    print(ans)
    print()
    
if __name__ == '__main__':
    t(tree_from_list([1, None, 2, 3]), [1,3,2])
    t(tree_from_list([1, None, 2, 3, 4, None, 5]), [1, 3, 5, 2, 4])
    print(tree_to_list(tree_from_list([1, None, 2, 3, 4, None, 5])))