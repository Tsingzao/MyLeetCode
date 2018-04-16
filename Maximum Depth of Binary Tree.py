# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:20:26 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nodes = [root]
        depth = 0
        while nodes:
            level = []
            while nodes:
                node = nodes.pop()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            depth = depth + 1
            nodes = level
        return depth