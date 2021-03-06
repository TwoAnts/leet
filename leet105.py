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
    
def build_tree(preorder, inorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    index = inorder.index(preorder[0])
    root.left = build_tree(preorder[1:1+index], inorder[:index])
    root.right = build_tree(preorder[1+index:], inorder[index+1:])
    return root
    
def t(p, i, ans):
    print(tree_to_list(build_tree(p, i)))
    print(ans)
    print()
    
if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    ans = [3, 9, 20, None, None, 15, 7]
    t(preorder, inorder, ans)