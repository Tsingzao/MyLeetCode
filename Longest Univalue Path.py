# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:24:13 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = 0
        def dfs(root):
            if not root:
                return 0
            m, n = dfs(root.left), dfs(root.right)
            m = m + 1 if root.left and root.left.val == root.val else 0
            n = n + 1 if root.right and root.right.val == root.val else 0
            self.ret = max(self.ret, m + n)
            return max(m, n)
        dfs(root)
        return self.ret