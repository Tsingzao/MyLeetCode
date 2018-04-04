# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 13:06:13 2018

@author: Tsingzao
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        f = 0
        l = len(numbers)-1
        while 1:
            if numbers[f] + numbers[l] > target:
                l = l - 1
            if numbers[f] + numbers[l] < target:
                f = f + 1
            if numbers[f] + numbers[l] == target:
                return [f+1,l+1]