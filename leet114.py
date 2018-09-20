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
    
def flatten(root):
    def core(root):
        if not root:
            return None
        first = root
        second = core(root.left)
        third = core(root.right)
        first.left = None
        first.right = second
        it = first
        while it.right:
            it = it.right
        it.right = third
        return first
    
    core(root)
    
def t(root, ans):
    flatten(root)
    print(tree_to_list(root))
    print(ans)
    print()
    
if __name__ == '__main__':
    ans = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
    t(tree_from_list([1, 2, 5, 3, 4, None, 6]), ans)