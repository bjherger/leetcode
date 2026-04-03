"""
Start: 16:57
End: 16:52

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
 - Count of 1 is not compressed (e.g. a -> a )
 - Individual digits are stored separately, e.g. a, 3, b, 1, 2
 - Do not need to susbset chars to only include returned answer

Options
 - Loop pointer. 2 variables: current group and count. Update as appropraite
   - T: O(n)
   - S: O(1) (no new space for result, using existing array)

Notes for next time:
  - Third attempt, just for polish. I really should be able to write this in one go
"""

from typing import List
from unittest import TestCase

def write_result(chars, write_index, group, count):
    chars[write_index] = group
    write_index += 1
    if count > 1:
        for digit in str(count):
            chars[write_index] = digit
            write_index += 1
    return write_index

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return 1
        
        read_index = 0
        write_index = 0
        group = chars[0]
        count = 1

        while read_index <= len(chars):
            read_index += 1
            # No more characters to read
            if read_index == len(chars):
                write_index = write_result(chars, write_index, group, count)
                break
            # Current character matches
            elif chars[read_index] == group:
                count += 1
            # Current character does not match
            else:
                next_group = chars[read_index]
                write_index = write_result(chars, write_index, group, count)
                group = next_group
                count = 1
        return write_index

tc = TestCase()
c1 = ["a", "a", "b", "b", "c", "c", "c"]
n1 = Solution().compress(c1)

tc.assertEqual(n1, 6)
tc.assertEqual(c1[:n1], ["a", "2", "b", "2", "c", "3"])

c2 = ["a"]
n2 = Solution().compress(c2)
tc.assertEqual(n2, 1)
tc.assertEqual(c2[:n2], ["a"])

c3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
n3 = Solution().compress(c3)
tc.assertEqual(n3, 4)
tc.assertEqual(c3[:n3], ["a", "b", "1", "2"])

