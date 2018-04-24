# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:05:47 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.equalSum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
    def equalSum(self, root, sum):
        if root:
            return int(root.val == sum) + self.equalSum(root.left, sum-root.val) + self.equalSum(root.right, sum-root.val)
        return 0