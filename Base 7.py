# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:09:33 2018

@author: Tsingzao
"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num > 0:
            ret = [""]
        else:
            ret = ['-']
        num = abs(num)

        while num:
            ret.insert(1,str(num%7))
            num = num // 7
        return "".join(ret)