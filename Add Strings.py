# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 08:36:29 2018

@author: Tsingzao
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        if len(num1) < len(num2):
            temp = num1
            num1= num2
            num2= temp
            del temp

        ret = []
        flag = False
        for i in range(len(num1)):
            if i < len(num2):
                temp = int(num1[i]) + int(num2[i])
            else:
                temp = int(num1[i])
            if flag:
                temp = temp + 1
            if temp > 9:
                cur = temp % 10
                flag = True
            else:
                cur = temp
                flag = False
            ret.append(str(cur))
        if flag:
            ret.append('1')
        ret = ret[::-1]
        ret = "".join(ret)
        return ret