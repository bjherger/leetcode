"""

Start: 3:15
End:

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
 - Lots of small details to keep track of
   - Python string indexing
   - Replication can be multiple digits. Need to find where the digits start and stop
   - Brackets can be nested. Need to find the matching end bracket
   - Brackets can also be sequential - can't just take the last bracket, as that could be for an unrelated open bracket
   - Would it have been easier to use a more explicit stack?
   - What is the complexity of this solution?

"""
import numbers
from typing import List
from unittest import TestCase

NUMBERS = set('1234567890')


def decodeHelper(s, start_index , end_index):
    # print(s[start_index:end_index], s, start_index, end_index)

    decoded = ""
    cursor = start_index

    while cursor <= end_index:

        if s[cursor] in NUMBERS:
            replication_left = cursor
            replication_right = cursor
            while s[replication_right + 1] in NUMBERS:
                replication_right += 1
            replication = int(s[replication_left:replication_right+1])
            # print(replication)
            left_bracket_index = replication_right + 1
            num_open_brackets = 1  # we're inside the '[' at left_bracket_index - 1

            for right_bracket_index in range(left_bracket_index + 1, end_index + 1, 1):
                if s[right_bracket_index] == '[':
                    num_open_brackets += 1
                elif s[right_bracket_index] == ']':
                    num_open_brackets -= 1
                    if num_open_brackets == 0:
                        break
            
            decoded += replication * decodeHelper(s, left_bracket_index + 1, right_bracket_index - 1)
            cursor = right_bracket_index
        else:
            if s[cursor] not in set('[]'):
                decoded += s[cursor]
            
        cursor += 1
    return decoded

class Solution:
    def decodeString(self, s: str) -> str:
        return decodeHelper(s, 0, len(s) -1)


# Tests
tc = TestCase()
s = Solution()

tc.assertEqual(
    s.decodeString(
        s = ""
    ),
    "",
)

tc.assertEqual(
    s.decodeString(
        s = "a"
    ),
    "a",
)

tc.assertEqual(
    s.decodeString(
        s = "3[a]"
    ),
    "aaa",
)

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

tc.assertEqual(
    s.decodeString(
        s="2[abc]3[cd]ef"
    ),
    "abcabccdcdcdef",
)

tc.assertEqual(
    s.decodeString(
        s="100[leetcode]"
    ),
   "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"
)

tc.assertEqual(
    s.decodeString(
        s="3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    ),
   "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
)