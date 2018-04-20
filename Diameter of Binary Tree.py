# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 17:09:52 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.p = 0
        def dfs(root):
            if not root:
                return 0
            m, n = dfs(root.left), dfs(root.right)
            self.p = max(self.p, m+n)
            return 1 + max(m,n)
        dfs(root)
        return self.p