# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 16:36:53 2018

@author: Tsingzao
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        key_value = {}
        for i in range(len(nums)):
            if nums[i] in key_value.keys() and i-key_value[nums[i]] <= k:
                return True
            key_value[nums[i]] = i
        return False
        '''
        key_value = {}
        for i, key in enumerate(nums):
            if key in key_value and i - key_value[key] <= k:
                return True
            key_value[key] = i
        return False