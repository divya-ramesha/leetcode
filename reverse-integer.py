"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: 
[−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        neg = False
        if x < 0:
            neg = True
            x = -x
        while x > 9:
            rem = x % 10
            num = num * 10 + rem
            x = x / 10
        num = num * 10 + x
        if neg:
            num = -num
        if(abs(num) > (2 ** 31 - 1)):
            return 0
        return num
