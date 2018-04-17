# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:04:16 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.val = 0
        def cum(root):
            if not root:
                return 0
            else:
                left, right = cum(root.left), cum(root.right)
                self.val = self.val + abs(left-right)
                return root.val + left + right
        cum(root)
        return self.val