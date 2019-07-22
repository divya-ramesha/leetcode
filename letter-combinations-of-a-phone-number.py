"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

class Solution(object):
    output = []
    num_to_letters = {}
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        self.output = []
        self.num_to_letters["2"] = ['a', 'b', 'c']
        self.num_to_letters["3"] = ['d', 'e', 'f']
        self.num_to_letters["4"] = ['g', 'h', 'i']
        self.num_to_letters["5"] = ['j', 'k', 'l']
        self.num_to_letters["6"] = ['m', 'n', 'o']
        self.num_to_letters["7"] = ['p', 'q', 'r', 's']
        self.num_to_letters["8"] = ['t', 'u', 'v']
        self.num_to_letters["9"] = ['w', 'x', 'y', 'z']
        
        list_of_digits = []
        for ch in digits:
            list_of_digits.append(ch)
        self.backtrack("", list_of_digits)
        return self.output
    
    def backtrack(self, comb, list_of_digits):
        if len(list_of_digits) == 0:
            self.output.append(comb)
        else:
            letters = self.num_to_letters[list_of_digits[0]]
            for i in letters:
                self.backtrack(comb + i, list_of_digits[1:])
            
            
