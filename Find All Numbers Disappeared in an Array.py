# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 17:55:08 2018

@author: Tsingzao
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        return list(i+1 for i in xrange(len(nums)) if nums[i] > 0)