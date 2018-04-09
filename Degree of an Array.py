# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 13:33:35 2018

@author: Tsingzao
"""

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        d = max(c.values())

        f = {}
        l = {}
        for i, n in enumerate(nums):
            f.setdefault(n, i)
            l[n] = i

        return min(l[v]-f[v]+1 for v in c if c[v] == d)