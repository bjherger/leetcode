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

"""

from unittest import TestCase


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) < 1:
            return True
        if len(t) < 1:
            return False

        start_index = 0
        s_index = 0
        t_index = 0

        while start_index +1 <= len(t):
            while t_index + 1 <= len(t):
                if t[t_index] == s[s_index]:
                    s_index += 1
                
                if s_index == len(s):
                    return True

                t_index +=1 
            
            start_index += 1
            t_index = start_index
            s_index = 0

        return False


tc = TestCase()
s = Solution()
tc.assertEqual(s.isSubsequence("abc", "ahbgdc"), True)
tc.assertEqual(s.isSubsequence("axc", "ahbgdc"), False)
tc.assertEqual(s.isSubsequence("b", "c"), False)