# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:31:00 2018

@author: Tsingzao
"""

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        def dfs(node, path):
            if node == len(graph) - 1:
                ret.append(path)
            else:
                for n in graph[node]:
                    dfs(n, path+[n])
        dfs(0, [0])
        return ret