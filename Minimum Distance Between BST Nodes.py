# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 11:06:44 2018

完全一样跟Minimum Absolute Difference in BST

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(root, vals=[]):
            if root.left:
                inorder(root.left, vals)
            vals.append(root.val)
            if root.right:
                inorder(root.right, vals)
            return vals
        vals = inorder(root)
        return min([abs(a-b) for a,b in zip(vals,vals[1:])])