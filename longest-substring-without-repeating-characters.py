"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
             
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substring = current_substring = ""
        for c in s:
            if c in current_substring:
                if len(current_substring) > len(longest_substring):
                    longest_substring = current_substring
                current_substring = current_substring[current_substring.index(c) + 1:] + c
            else:
                current_substring += c
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
        return len(longest_substring)
      
      
##################################  OR  ##########################################

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substring = start = 0
        charMap = {}
        for index, c in enumerate(s):
            if c in charMap and charMap[c] >= start:
                longest_substring = max(longest_substring, index - start)
                start = charMap[c] + 1
            charMap[c] = index
        longest_substring = max(longest_substring, len(s) - start)
        return longest_substring
