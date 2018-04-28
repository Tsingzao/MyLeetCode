# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 15:06:07 2018

@author: Tsingzao
"""

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sa = a.strip('i').split('+')
        sb = b.strip('i').split('+')
        return str(int(sa[0])*int(sb[0])-int(sa[1])*int(sb[1]))+'+'+str(int(sa[0])*int(sb[1])+int(sa[1])*int(sb[0]))+'i'