# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 18:46:21 2018

@author: Tsingzao
"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = collections.Counter(nums)
        ret = 0
        for num in cnt:
            if num+1 in cnt:
                ret = max(ret, cnt[num]+cnt[num+1])
        return ret