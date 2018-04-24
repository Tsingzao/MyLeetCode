# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:51:34 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if (not s and t) or (s and not t):
            return False
        return (s.val == t.val) and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        if t and not s:
            return False
        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)