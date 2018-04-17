# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 19:42:41 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        nodes = [root]
        size = 1
        while len(nodes)>0:
            temp = []
            tmp = []
            cnt = 0
            while size > 0:
                node = nodes.pop(0)
                size = size - 1
                tmp.append(node.val)
                if node.left:
                    nodes.append(node.left)
                    cnt = cnt + 1
                if node.right:
                    nodes.append(node.right)
                    cnt = cnt + 1
            ret.append(tmp)
            size = cnt
        return ret[::-1]