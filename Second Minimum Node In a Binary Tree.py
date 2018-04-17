# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 20:17:55 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = []
        if not root:
            return None
        nodes = [root]
        size = 1
        while len(nodes) > 0:
            cnt = 0
            while size > 0:
                node = nodes.pop(0)
                size = size - 1
                ret.append(node.val)
                if node.left:
                    nodes.append(node.left)
                    cnt = cnt + 1
                if node.right:
                    nodes.append(node.right)
                    cnt = cnt + 1
            size = cnt
        if len(set(ret)) == 1:
            return -1
        else:
            temp = sorted(set(ret))
            return temp[1]