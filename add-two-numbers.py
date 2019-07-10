"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        response = ListNode(0)
        head = response
        while l1 or l2 or carry:
            if l1 == None:
                num1 = 0
            else:
                num1 = l1.val
                l1 = l1.next
            if l2 == None:
                num2 = 0
            else:
                num2 = l2.val
                l2 = l2.next
            added_val = num1 + num2 + carry
            if added_val > 9:
                carry = added_val // 10
                added_val = added_val % 10
            else:
                carry = 0
            response.next = ListNode(added_val)
            response = response.next
        return head.next
