# -*- coding: utf-8 -*-
"""
Created on Sat Apr 07 19:39:59 2018

@author: Tsingzao
"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])