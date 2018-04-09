# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 23:02:22 2018

@author: Tsingzao
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums))-sum(nums)