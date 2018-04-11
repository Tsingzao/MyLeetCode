# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 14:16:18 2018

@author: Tsingzao
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = None
        while slow:
            late = slow.next
            slow.next = tail
            tail = slow
            slow = late
        while tail:
            if tail.val != head.val:
                return False
            tail = tail.next
            head = head.next
        return True