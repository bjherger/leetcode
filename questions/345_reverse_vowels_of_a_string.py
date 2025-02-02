"""
https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Constraints
 - vowels = aeiou, can be upper or lower case
Questions
 - No y
 - If no vowels, do nothing
 - If one vowel, same place
Options
 - Brute force: Two pointers, one from front and another from the back. Iterate until vowels are found, and switch. Could be difficult edge cases / inelegant. T: O(n), S: O(n) (assuming we're not modifying orignial string)
 - Two pass Do a forward pass and store vowels in an array. Reverse the array. Perform a second pass and replace each variable with next up in the array. T: O(n), S: O(n)
 - Two pass, different data structure: Could use a doubly linked list, stack. No speed up if vowel array is pre-created to the right size, not sure if Python has these data types built in

 Will implement two pass w/ array
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # Optimization: Create array of same length as s, keep track of which index is next
        vowels_found = list()
        return_list = list()

        vowels = set('aeiouAEIOU')
        for c in s:
            if c in vowels:
                vowels_found.append(c)
        
        vowels_found_index = len(vowels_found) - 1
        for c in s:
            if c not in vowels:
                return_list.append(c)
            else:
                return_list.append(vowels_found[vowels_found_index])
                vowels_found_index -=1
        return ''.join(return_list)
s = Solution()

assert(s.reverseVowels('IceCreAm') == 'AceCreIm') 
assert(s.reverseVowels('leetcode') == 'leotcede') 