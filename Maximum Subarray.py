# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 09:24:19 2018

@author: Tsingzao
"""

'''==========这里只要求返回最大值，没要求序列================'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = c = -10000000000
        for n in nums:
            l = max(n, l+n)
            c = max(l, c)
        return c