# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 09:34:21 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        ret = ""
        if not t:
            return ""
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left or right:
            if not left:
                ret = ret + '()'
            else:
                ret = ret + '(' + left + ')'
        if right:
            ret = ret + '(' + right + ')'
        return str(t.val) + ret