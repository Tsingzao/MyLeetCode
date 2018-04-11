# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:22:47 2018

@author: Tsingzao
"""

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        temp = []
        for op in ops:
            if op not in ["C","D","+"]:
                temp.append(int(op))
            if op == "C":
                temp = temp[:-1]
            if op == "D":
                temp.append(2*temp[-1])
            if op == "+":
                temp.append(temp[-1]+temp[-2])
        return sum(temp)
