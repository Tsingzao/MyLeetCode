# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:07:42 2018

@author: Tsingzao
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        ret = ""
        rng = 10000000
        flag = True
        for i in range(len(strs)):
            tmp = len(strs[i])
            rng = tmp if tmp < rng else rng
            flag = True
        for i in range(rng):
            tmp = strs[0][i]
            for j in range(1,len(strs)):
                if tmp == strs[j][i]:
                    continue
                else:
                    flag = False
                    break
            if not flag:
                break
            ret = ret + tmp
        return ret