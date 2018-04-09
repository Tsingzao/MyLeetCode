# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 18:52:57 2018

@author: Tsingzao
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        s = sum(nums)
        n = 0
        for i in xrange(len(nums)):
            if (s - nums[i]) == n*2:
                return i
            n = n + nums[i]
        return -1