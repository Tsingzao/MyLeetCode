# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:36:23 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.val = 0
        def inorder(root):
            if root:
                inorder(root.left)
                if root.left and not root.left.left and not root.left.right:
                    self.val = self.val + root.left.val
                inorder(root.right)
        inorder(root)
        return self.val