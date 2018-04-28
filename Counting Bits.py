# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:17:41 2018

@author: Tsingzao
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def countOnes(num):
            cnt = 0
            while num:
                num = num & (num - 1)
                cnt += 1
            return cnt
        ret = []
        for i in range(num+1):
            ret.append(countOnes(i))
        return ret