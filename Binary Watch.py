# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:49:14 2018

@author: Tsingzao
"""

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        for hour in range(12):
            for minute in range(60):
                if (bin(hour)+bin(minute)).count('1') == num:
                    ret.append('%d:%02d' % (hour, minute))
        return ret