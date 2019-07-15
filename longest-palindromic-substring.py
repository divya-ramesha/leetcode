"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s

        res = ""
        s_len = len(s)
        for i in range(s_len):
            j = i + 1
            res_len = len(res)
            while j <= s_len and res_len <= len(s[i:]):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > res_len:
                    res = s[i:j]
                j += 1

        return res
