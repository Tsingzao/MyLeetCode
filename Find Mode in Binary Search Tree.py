# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 21:04:13 2018

@author: Tsingzao
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cnt = collections.Counter()
        def dfs(root):
            if root:
                cnt[root.val] = cnt[root.val] + 1
                dfs(root.left)
                dfs(root.right)
        if root:
            dfs(root)
            max_ct = max(cnt.itervalues())
            return [k for k, v in cnt.iteritems() if v == max_ct]
        return []