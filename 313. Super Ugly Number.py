#!/usr/bin/env python
# encoding: utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先判空，否则会出错
        if head == None oimpor head.next == None:
            return head
        prev = head
        p = head.next
        while p != None:
            if p.val == prev.val:
                prev.next = p.next
                p = p.next
            else:
                prev = p
                p = p.next
        return head