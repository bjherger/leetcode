"""

Start: 2:14
End: 3:00 (didn't finish)

https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

Questions / notes:

 - Can be recursive / nested: Yes
 - Numbers inside of "repeats": No
 - Edge case: Empty input string: Return empty stirng
 - Edge case: Invalid input: Won't happen
 - Edge case: String w/o repeats: Just append
 - Note: Either stack or recursion

Options
 - Option 1: Brute force - Many passes, track deepest nesting, deecode inner most layers, then keep passing
  - T: O()
  - S: O()
  - Can we do better? Probably. This is messy to implement, unclear
 - Option 2: Recursive: Create helper function. On each number, pass in. Base case: No brackets / number
   - T: O(300^10) = constant (?)
   - S: O(300^10) = constant (?)
   - Can we do better? Probably not
 

Edge cases

 - 

Notes

 - God this is messy
 - Lots of little details around whether to include the end index or not
 - Will just start from scratch again

"""
from tracemalloc import start
from typing import List
from unittest import TestCase

NUMBERS = set('123456789')


def decodeHelper(s, start_index , end_index):
    print()
    print(s, start_index, end_index, s[start_index:end_index])
    decoded = ""
    cursor = start_index

    if start_index > end_index:
        return decoded
    
    while cursor <= end_index and cursor < len(s):
        print(cursor)
        if s[cursor] in NUMBERS:
            repeat_count = int(s[cursor])
            start_bracket_index = cursor + 1
            for close_bracket_index in range(start_bracket_index, end_index):
                if s[close_bracket_index] == ']':
                    break
            decoded += repeat_count * decodeHelper(s, start_bracket_index + 1, close_bracket_index-1)
            cursor = close_bracket_index
        else:
            decoded += s[cursor]
        
        cursor += 1

    return decoded

class Solution:
    def decodeString(self, s: str) -> str:
        return decodeHelper(s, 0, len(s))


# Tests
tc = TestCase()
s = Solution()

# tc.assertEqual(
#     s.decodeString(
#         s = ""
#     ),
#     "",
# )

# tc.assertEqual(
#     s.decodeString(
#         s = "a"
#     ),
#     "a",
# )

# tc.assertEqual(
#     s.decodeString(
#         s = "3[a]"
#     ),
#     "aaa",
# )

tc.assertEqual(
    s.decodeString(
        s = "3[a]2[bc]"
    ),
    "aaabcbc",
)

tc.assertEqual(
    s.decodeString(
        s = "3[a2[c]]"
    ),
    "accaccacc",
)

# tc.assertEqual(
#     s.decodeString(
#         s="2[abc]3[cd]ef"
#     ),
#     "abcabccdcdcdef",
# )

