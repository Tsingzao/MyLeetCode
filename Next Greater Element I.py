# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:32:08 2018

@author: Tsingzao
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = []
        for num in findNums:
            for i in range(nums.index(num),len(nums)):
                if nums[i] > num:
                    temp.append(nums[i])
                    break
                else:
                    if i == len(nums) - 1:
                        temp.append(-1)
        return temp
    