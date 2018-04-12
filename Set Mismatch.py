# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 09:39:20 2018

@author: Tsingzao
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bias = sum([i+1 for i in range(len(nums))]) - sum(nums)
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 0:
                break
        return [nums[i], bias+nums[i]]