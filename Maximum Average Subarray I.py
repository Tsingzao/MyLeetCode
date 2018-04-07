# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 20:24:04 2018

@author: Tsingzao
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        s = sum(nums[:k])
        t = s
        for i in xrange(len(nums)-k):
            t = t - nums[i] + nums[i+k]
            if t > s:
                s = t
        return s*1.0/k
