# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 17:17:46 2018

@author: Tsingzao
"""

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ct = collections.Counter(nums)
        if k < 0:
            return 0
        if k == 0:
            return sum(ct[i] > 1 for i in ct)
        if k > 0:
            return sum(i+k in ct for i in ct)        