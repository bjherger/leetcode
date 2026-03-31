"""
Start: 15:40
End: TODO

https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=leetcode-75

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

Constraints:

- 0 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

Questions / notes:
 - Kind of a super set. Need to write mapping from each number to relevant letters
 - Number can map to 3 or 4 letters

Options
 - O1: Brute force. Walk through number by number. For each number look up mapped letters. For each mapped letter, create a copy of exist results, extend w/ that letter
   - T: O(n*4^n) (each number can be up to 4 letters)
   - S: O(n*4^n)
 - O2: Bakctracking. Build 0th character for each, then swap

Notes for next time:
"""

from itertools import product
from typing import List
from unittest import TestCase

mapping = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        results = []
        path = []

        def backtrack(i):
            if len(path) == len(digits):
                results.append("".join(path))
                return
            digit = digits[i]
            for j in mapping[digit]:
                path.append(j)
                backtrack(i+1)
                path.pop()
        
        backtrack(0)
        return results


tc = TestCase()
tc.assertEqual(
    Solution().letterCombinations("23"),
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
)
tc.assertEqual(Solution().letterCombinations(""), [])
tc.assertEqual(Solution().letterCombinations("2"), ["a", "b", "c"])

# "Pretty long" (max length per constraints). Order can be any, so compare sorted.
digits = "9999"
expected = ["".join(p) for p in product(*(mapping[d] for d in digits))]
tc.assertEqual(sorted(Solution().letterCombinations(digits)), sorted(expected))

