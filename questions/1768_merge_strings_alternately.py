# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

class Solution:
    """
    Constraints: N/A
    Questions: N/A
    Options: 
        1) Increase index. T: O(n+m), S: O(n+m) (does pythong have a string builder?)
    """
    
    def mergeAlternately(self, word1: str, word2: str) -> str:

        new_word_list = list()
        i=0
        max_index = max([len(word1), len(word2)])
        while i < max_index:
            if i < len(word1):
                new_word_list.append(word1[i])
            if i < len(word2):
                new_word_list.append(word2[i])
            i += 1

        return ''.join(new_word_list)