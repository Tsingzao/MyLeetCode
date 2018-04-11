# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:43:50 2018

@author: Tsingzao
"""

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.data.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        temp = self.data[0]
        self.data = self.data[1:]
        return temp

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.data[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.data) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()