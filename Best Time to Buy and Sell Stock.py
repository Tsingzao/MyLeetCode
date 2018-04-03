# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 20:14:28 2018

@author: Tsingzao
"""

'''==============转换成最大子集问题================'''
'''==============即元素差的最大子集================'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur = 0
        sf  = 0
        for i in range(1,len(prices)):
            cur = max(0, prices[i] - prices[i-1] + cur)
            sf = max(cur, sf)

        return sf