# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 15:19:15 2018

@author: Tsingzao
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key_value = {}
        for num in nums:
            if not num in key_value.keys():
                key_value[num] = 1
            else:
                key_value[num] = key_value[num] + 1
        for key in key_value.keys():
            if key_value[key]>len(nums)//2:
                return key