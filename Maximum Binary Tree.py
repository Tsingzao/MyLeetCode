# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 13:52:24 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            root = TreeNode(max(nums))
            root.left = self.constructMaximumBinaryTree(nums[:nums.index(max(nums))])
            root.right = self.constructMaximumBinaryTree(nums[nums.index(max(nums))+1:])
            return root