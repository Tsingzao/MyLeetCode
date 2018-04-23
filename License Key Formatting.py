# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 09:03:17 2018

@author: Tsingzao
"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        lst = S.upper().replace('-','')
        l = len(lst)%K
        ret = [lst[:l]]
        while l<len(lst):
            ret.append(lst[l:l+K])
            l = l+K
        ret = "-".join(ret)
        if ret == '':
            return ret
        if ret[0] == '-':
            return ret[1:]
        return ret
