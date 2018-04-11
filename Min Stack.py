# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:02:54 2018

@author: Tsingzao
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        temp = self.data[-1]
        self.data = self.data[:-1]
        return temp

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.data)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()