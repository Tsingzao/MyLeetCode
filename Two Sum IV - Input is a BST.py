# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:39:31 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        elements = []
        nodes = [root]
        while nodes:
            level = []
            while nodes:
                node = nodes.pop()
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                elements.append(node.val)
            nodes = level
        for e in elements:
            if k == 2 * e:
                temp = collections.Counter(elements)
                if temp[e] > 1:
                    return True
            else:
                if k-e in elements:
                    return True
        return False