"""
Start: 15:39
End: 16:29

https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead be stored in the input
character array chars. Note that group lengths that are 10 or longer will be split into
multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be:
["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is a single character "a", which remains uncompressed since it's
a single character.

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"]
Explanation: The groups are "a" and "bbbbbbbbbbbb" (12 b's). This compresses to "ab12".

Constraints:

- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol

Questions / notes:
 - Store answer in place (ie use existing array)
 - Can group be multiple characters? Unclear
 - Return new array - no. Return length of new array
 - Why create the compressed array at all? We could just count the length of the new array that would be generated
 - ab12 will be saved as a, b, 1, 2

Options
 - Loop pointer. 2 variables: current group and count. Update as appropraite
   - T: O(n)
   - S: O(1) (no new space for result, using existing array)

Notes for next time:
 -
"""

from typing import List
from unittest import TestCase


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        i = 0
        g = chars[0]
        c = 1
        rl = 0
        chars_i = 0

        while i < len(chars):
            i += 1

            if  i == len(chars):
                chars[chars_i] = g
                chars[chars_i+1] = str(c)
                rl += 1 + len(str(c)) # Count can include multiple digits
            elif chars[i] == g:
                c += 1
            else:
                new_g = chars[i]
                chars[chars_i] = g
                rl += 1
                chars_i += 1
                if c != 1:
                    for j in str(c):
                        print(j, chars_i)
                        chars[chars_i] = j
                        print(chars)
                        rl += 1
                        chars_i += 1
                g = new_g
                c = 1
        return rl


tc = TestCase()
# c1 = ["a", "a", "b", "b", "c", "c", "c"]
# n1 = Solution().compress(c1)
# tc.assertEqual(n1, 6)
# tc.assertEqual(c1[:n1], ["a", "2", "b", "2", "c", "3"])

# c2 = ["a"]
# n2 = Solution().compress(c2)
# tc.assertEqual(n2, 1)
# tc.assertEqual(c2[:n2], ["a"])

c3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
n3 = Solution().compress(c3)
tc.assertEqual(n3, 4)
tc.assertEqual(c3[:n3], ["a", "b", "1", "2"])
