# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:11:23 2018

@author: Tsingzao
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            temp = a
            a = b
            b = temp
            del temp
        a = a[::-1]
        b = b[::-1]
        ret = []
        flag = False
        for i in range(len(a)):
            if i < len(b):
                temp = int(a[i])+int(b[i])
            else:
                temp = int(a[i])
            if flag:
                temp = temp+1
            if temp > 1:
                temp = temp%2
                flag = True
                ret.append(str(temp))
            else:
                ret.append(str(temp))
                flag = False
        if flag:
            ret.append("1")
        ret = ret[::-1]
        return "".join(ret)