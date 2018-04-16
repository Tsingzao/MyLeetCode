# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:15:50 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        nodes = [root]
        while nodes:
            level = []
            vals = 0
            cnt = 0
            while nodes:
                node = nodes.pop()
                if node.left: 
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                vals = vals + node.val
                cnt = cnt + 1
            ret.append(vals*1.0/cnt)
            nodes = level
        return ret