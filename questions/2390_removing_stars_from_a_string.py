"""

Start: 3:10
End: 3:19. 

https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

You are given a string s, which contains stars *.

In one operation, you can:

 - Choose a star in s.
 - Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.

Questions / notes:
 - Empty string: Won't happen / can return immediately


Options
 - Option 1: Two pointers. Sweep l and r until a star is found, remove until no more stars. Continue sweeping / going back. Convert back to string
   - T: O(n)
   - S: O(n)
   - Can we do better: Probably not. But this is listed under stacks
- Option 2: Add letters to a stack. If a star is encountered, remove the top of the stack before continuing. Re-assemble stirng
   - T: O(n)
   - S: O(n)
   - Can we do better: Probably not.


Edge cases

 - 

Notes

 - The pointer system would have worked, but the stack is much cleaner
 - This was scary at first, but easy to implement
 

"""
from typing import List
from unittest import TestCase

class Solution:
    def removeStars(self, s: str) -> str:
        seen = list()
        for i in s:
            if i == '*':
                seen.pop()
                # Don't add the star!
            else:
                seen.append(i)
        return ''.join(seen)

# Tests
tc = TestCase()
s = Solution()

tc.assertEqual(
    s.removeStars(
       s = "leet**cod*e"
    )
    , "lecoe"
    )


tc.assertEqual(
    s.removeStars(
        s = "erase*****"
    )
    , ""
    )