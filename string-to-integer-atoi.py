"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        neg = False
        num = 0
        if not str:
            return 0
        if str[0] == "+":
            str = str[1:]
        elif str[0] == "-":
            neg = True
            str = str[1:]
        if not str:
            return 0
        if str[0] != "1" and str[0] != "2" and str[0] != "3" and str[0] != "4" and str[0] != "5" and str[0] != "6" and str[0] != "7" and str[0] != "8" and str[0] != "9" and str[0] != "0":
            return 0
        while str and str[0] == "0":
            str = str[1:]
        if not str:
            return 0
        extra = 0
        for ch in str:
            if ch == "1":
                extra = 1
            elif ch == "2":
                extra = 2
            elif ch == "3":
                extra = 3
            elif ch == "4":
                extra = 4
            elif ch == "5":
                extra = 5
            elif ch == "6":
                extra = 6
            elif ch == "7":
                extra = 7
            elif ch == "8":
                extra = 8
            elif ch == "9":
                extra = 9
            elif ch == "0":
                extra = 0
            else:
                extra = None
            if extra == None:
                break
            num = num * 10 + extra
        if neg:
            num = num * -1
        INT_MAX = pow(2, 31) - 1
        INT_MIN = pow(-2, 31)
        if (num > INT_MAX):
            return INT_MAX
        elif (num < INT_MIN):
            return INT_MIN
        return num
            
