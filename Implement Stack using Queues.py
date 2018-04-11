# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:57:01 2018

@author: Tsingzao
"""

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = list()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        temp = self.data[-1]
        self.data = self.data[:-1]
        return temp

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.data[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.data) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()