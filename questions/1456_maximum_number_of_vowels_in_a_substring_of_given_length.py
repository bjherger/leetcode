"""

Start: 4:35
End: 4:46

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

Questions
 - Data validation: nums will be longer than K
 - Do not neet to keep or return positions of max


Options
 - Option 1: Brute force. Re-compute window each time
   - T: O(n*k)
   - S: O(1)
 - Option 2: Sliding window. Subract 1 if s[i] is a vowel, add 1 if s[i+k] is a vowel
   - T: O(n)
   - S: O(1)

Notes

 - Originally used < instead of <= in while loop
 - Vowel check method might be overkill. Also nice to avoid creating vowels each time
 - The type hint in the problem is wrong. It suggests an array of strings, really the examples are just 1 string
 - Could use python ternary if a few places


"""
from typing import List
from unittest import TestCase

VOWELS = set('aeiou')

def vowel_check(s):
    if s in VOWELS:
        return 1
    else:
        return 0


class Solution:
    def maxVowels(self, s: List[int], k: int) -> float:

        current_num_vowels = 0
        left_index = 0

        for i in range(k):
            current_num_vowels += vowel_check(s[i])

        max_num_vowels = current_num_vowels

        while left_index + k <= len(s) - 1:
            current_num_vowels = current_num_vowels - vowel_check(s[left_index]) + vowel_check(s[left_index + k])
            if current_num_vowels > max_num_vowels:
                max_num_vowels = current_num_vowels

            left_index += 1
        return max_num_vowels


tc = TestCase()
s = Solution()
# tc.maxVowels(type(s.maxVowels([1,8,6,2,5,4,8,3,7])), int)
tc.assertEqual(s.maxVowels(s='abciiidef', k=3), 3)
tc.assertEqual(s.maxVowels(s='aeiou', k=2), 2)
tc.assertEqual(s.maxVowels(s='leetcode', k=3), 2)
tc.assertEqual(s.maxVowels(s='weallloveyou', k=7), 4)