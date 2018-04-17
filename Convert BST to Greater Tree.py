# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:13:40 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.vals = 0
        def cumsum(root):
            if root:
                cumsum(root.right)
                root.val = root.val + self.vals
                self.vals = root.val
                cumsum(root.left)
        cumsum(root)
        return root