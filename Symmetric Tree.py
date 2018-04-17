# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:32:34 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        nodes = [[root.left, root.right]]
        while nodes:
            [left, right] = nodes.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val == right.val:
                nodes.insert(0, [left.left, right.right])
                nodes.insert(0, [left.right, right.left])
            else:
                return False
        return True