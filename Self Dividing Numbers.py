# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:08:35 2018

@author: Tsingzao
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left, right+1):
            j = i
            tmp = []
            while i:
                tmp.append(i%10)
                i = i // 10
            if 0 in tmp:
                continue
            else:
                flag = True
                for tp in tmp:
                    if j % tp == 0:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    ret.append(j)
        return ret