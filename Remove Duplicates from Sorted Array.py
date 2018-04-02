# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 09:05:00 2018

我尼玛，理解能力有待提高，看了题目还以为让返回列表元素，
就有了以下**代码，后来看解析才知道。。。>_<。。。

@author: Tsingzao
"""

#==============================================================================
# nums = [1,1,2]
# for i in range(len(nums))[::-1]:
#     if nums[i] in nums[:i]:
#         nums = nums[:i]+nums[i+1:]
# print nums
#==============================================================================

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        j = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j = j+1
        return j+1