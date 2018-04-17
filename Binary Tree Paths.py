# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:00:08 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        if not root:
            return []
        nodes = [(root,"")]
        while nodes:
            node,path = nodes.pop()
            if not node.left and not node.right:
                ret.append(path+str(node.val))
            if node.right:
                nodes.append((node.right, path+str(node.val)+"->"))
            if node.left:
                nodes.append((node.left, path+str(node.val)+"->"))
        return ret