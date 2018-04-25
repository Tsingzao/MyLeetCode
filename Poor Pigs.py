# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:06:51 2018

@author: Tsingzao
"""

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        import math
        return int(math.ceil(math.log(buckets,(minutesToTest//minutesToDie)+1)))