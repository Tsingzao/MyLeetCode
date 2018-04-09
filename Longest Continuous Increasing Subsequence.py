# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 11:01:45 2018

@author: Tsingzao
"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        mt = 1
        ct = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                ct = ct + 1
                if mt < ct:
                    mt = ct
            else:
                ct = 1
        return mt