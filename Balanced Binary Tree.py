# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:32:11 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #def depth(root):
        #    if not root:
        #        return 0
        #    return max(depth(root.left), depth(root.right))+1
        #if not root:
        #    return True
        #left = depth(root.left)
        #right = depth(root.right)
        #return abs(left-right)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1:
                return -1
            if abs(left-right)>1:
                return -1
            return max(left, right) + 1
        return dfs(root) != -1