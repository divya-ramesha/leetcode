"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        index = 0
        if len(strs) < 1:
            return ""
        min_len = len(strs[0])
        output = ""
        for s in strs:
            min_len = min(min_len, len(s))
        for i in range(min_len):
            same_char = True
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    same_char = False
                    break
            if same_char:
                output += char
            else:
                break
        return output
    
