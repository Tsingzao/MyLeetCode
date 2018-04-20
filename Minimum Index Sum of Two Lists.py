# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 20:55:54 2018

@author: Tsingzao
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        re = {rest: i for i,rest in enumerate(list1)}
        ze = {rest: i for i,rest in enumerate(list2)}
        we = {rest: re[rest]+ze[rest] for rest in list1 if rest in list2}
        id = min(we.values())
        ret = []
        for key in we:
            if we[key] == id:
                ret.append(key)
        return ret