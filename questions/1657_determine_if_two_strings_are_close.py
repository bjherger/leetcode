"""

Start: 12:21
End: 12:35

https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
Example 3:

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000


Questions / notes:
 - How many times can we apply operations - unlimited
 - Empty strings?
 - Must be same length. n1 = n2 = n = length of either string. If not, return false
 - Could just map to a new character set. What reallly matters is the distribution of unique letters
 - Letter order doesn't matter at all


Options
 - Option 1: Brute force. Create countercs c1 and c2. Check if value lists are equivalent (without sorting?)
   - T: O(n)
   - S: O(n)
   - Can we do better: Probably small optimizations, but probably not on time. Might be able to reduce number of copies, but still same space complexity

Edge cases

 - Empty strings. Same?

Notes

 - Originally missed +1 when adding values to counter
 - Originally missed requirement that both have the same set of characters. Re-reading, I don't feel very awful about having missed this - it's not very clear. 
 

"""
from typing import List
from unittest import TestCase

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = dict()
        c2 = dict()

        for i in word1:
            c1[i] = c1.get(i, 0) + 1
        
        for i in word2:
            c2[i] = c2.get(i, 0) + 1

        d1 = dict()
        d2 = dict()

        for i in c1.values():
            d1[i] = d1.get(i, 0) + 1

        for i in c2.values():
            d2[i] = d2.get(i, 0) + 1
        
        return d1 == d2 and set(c1.keys()) == set(c2.keys())

# Tests
tc = TestCase()
s = Solution()

tc.assertEqual(
    s.closeStrings(
       word1 = "abc", word2 = "bca"
    )
    , True
    )


tc.assertEqual(
    s.closeStrings(
        word1 = "a", word2 = "aa"
    )
    , False
    )

tc.assertEqual(
    s.closeStrings(
        word1 = "cabbba", word2 = "abbccc"
    )
    , True
    )

tc.assertEqual(
    s.closeStrings(
        word1 = "uau", word2 = "ssx"
    )
    , False
    )