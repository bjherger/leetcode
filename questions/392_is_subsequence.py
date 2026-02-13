"""

Start: 2:44
End: 3:11 (though I got distracted and was chatting)

https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

Questions
 - Character set: Doesn't really matter
 - Array sizes: Mentioned above
 - Input cleaning: Don't need to do any input cleaning

n = len(s)
m = len(t)

Options:
 - Option 1: Two pointers. Scan t once; for each char in s in order, find the next match in t (advance j until t[j]==s[i], then advance i). If we exhaust s, true; else false.
   - T: O(n + m) — each of s and t traversed at most once.
   - S: O(1)
   - Evaluation: Correct, optimal for single-query. No need to "skip" parts of s or t; one pass suffices. For the follow-up (many s, one t), preprocess t into e.g. char->sorted list of indices and binary-search per character for O(m + k*n*log(m)).


"""

from unittest import TestCase


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) < 1:
            return True
        if len(t) < 1:
            return False

        s_index = 0
        t_index = 0

        while s_index +1 <= len(s) and t_index + 1 <= len(t) :
            if t[t_index] == s[s_index]:
                s_index += 1
            
            if s_index == len(s):
                return True

            t_index +=1 

        return False


tc = TestCase()
s = Solution()
tc.assertEqual(s.isSubsequence("abc", "ahbgdc"), True)
tc.assertEqual(s.isSubsequence("axc", "ahbgdc"), False)
tc.assertEqual(s.isSubsequence("b", "c"), False)