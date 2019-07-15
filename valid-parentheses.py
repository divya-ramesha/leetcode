"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return True
        queue = []
        i = 1
        l = len(s)
        queue.append(s[0])
        while i < l:
            if not queue:
                queue.append(s[i])
                i += 1
                continue
            top = queue[-1]
            if s[i] == ")":
                if top == "(":
                    queue.pop()
                else:
                    return False
            elif s[i] == "}":
                if top == "{":
                    queue.pop()
                else:
                    return False
            elif s[i] == "]":
                if top == "[":
                    queue.pop()
                else:
                    return False
            else:
                queue.append(s[i])
            i += 1
        if queue:
            return False
        else:
            return True
            
