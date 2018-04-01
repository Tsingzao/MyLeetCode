# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 18:11:11 2018

@author: Tsingzao
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if target-nums[i] in nums and i!=nums.index(target-nums[i]):
                return [i, nums.index(target-nums[i])]