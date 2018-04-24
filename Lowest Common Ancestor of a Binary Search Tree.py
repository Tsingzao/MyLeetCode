# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:53:59 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while True:
            if root.val - p.val > 0 and root.val - q.val > 0:
                root = root.left
            elif root.val - p.val < 0 and root.val - q.val < 0:
                root = root.right
            else:
                break
        return root