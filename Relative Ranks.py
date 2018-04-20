# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:36:50 2018

@author: Tsingzao
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        temp = []
        temp[:] = nums[:]
        temp.sort()
        temp.reverse()

        for i,l in enumerate(nums):
            idx = temp.index(l)
            if idx == 0:
                nums[i] = 'Gold Medal'
            elif idx == 1:
                nums[i] = 'Silver Medal'
            elif idx == 2:
                nums[i] = 'Bronze Medal'
            else:
                nums[i] = str(idx+1)

        return nums 