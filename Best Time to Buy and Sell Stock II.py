# -*- coding: utf-8 -*-
"""
Created on Tue Apr 03 20:29:41 2018

@author: Tsingzao
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        pro = 0
        for i in range(1,len(prices)):
            pro = pro + max(0, prices[i]-prices[i-1])
        return pro
            