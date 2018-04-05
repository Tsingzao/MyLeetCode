# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 17:27:28 2018

@author: Tsingzao
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mct = 0
        ct = 0
        for num in nums:
            if num == 1:
                ct = ct + 1
                if ct > mct:
                    mct = ct
            if num == 0:
                ct = 0
        return mct