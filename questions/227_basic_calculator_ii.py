"""
https://leetcode.com/problems/basic-calculator-ii/description/

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Requirements
 
Questions
 - Signed (e.g. -1 * 12). No, positive integers
 - Parenthesis. No
Options

"""

class Solution:

    def evaluate_number(self, s:str) -> int: 
        return eval(s)

    def calculate(self, s: str) -> int:
        stack = list()
        n = 0
        operator = '+'
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

        for i, c in enumerate(s):
            if c in digits:
                n = n*10 + int(c)
            if c in set('+-*/') or i == len(s) - 1:
                print('here', c)
                if operator == '*':
                    stack.append(stack.pop() * n)
                elif operator == '/':
                    stack.append(stack.pop() / n)
                elif operator == '+':
                    stack.append(n)
                elif operator == '-':
                    stack.append(-1 * n)
                operator = c
                n = 0
                
        return sum(stack) 
    
s = Solution()
print(s.calculate('3*5'))
assert(s.calculate('3*5') == 15)
assert(s.calculate('3*5*2') == 30)