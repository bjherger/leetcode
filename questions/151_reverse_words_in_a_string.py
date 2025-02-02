"""
https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Constraints
 - Words separated by 1+ space characters
Questions
 - Non space whitespace characters (e.g. \n or \t)?. Assumng not
 - Empty string?
Options
 - This could be completed using Python built in fuctinos (e.g. split and reverse). I'll aim to complete by hand instead
 - Brute force: Iterate through string. If space, flush current word buffer to running list of words. If not space, add to current word buffer. Reverse list of words, concat. T: O(n), S: O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = list()
        word_buffer = list()
        for c in s:
            if c == ' ':
                if len(word_buffer) > 0:
                    word_list.append(''.join(word_buffer))
                    word_buffer = list()
            else:
                word_buffer.append(c)
        if len(word_buffer) > 0:
           word_list.append(''.join(word_buffer))
        return ' '.join(reversed(word_list))

s = Solution()
assert(s.reverseWords('the sky is blue') == 'blue is sky the')
assert(s.reverseWords('  hello world  ') == 'world hello')
assert(s.reverseWords('') == '')
assert(s.reverseWords(' ') == '')