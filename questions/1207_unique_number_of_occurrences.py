"""

Start: 12:12
End: 12:17

https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000


Questions:
 - Can use python counter?

Options
 - Option 1: Brute force. Create a hashmap / default dict w/ counts. Convert values to set, see if size of dict matches set of values
   - T: O(n)
   - S: O(n)
   - Can we do better: Probably need to touch every element, so time can't do much better. Could probably create fewer containers, but space complexity would be the same

Edge cases

 - Empty lists - at least 1 element

Notes

 - No tricks, pretty straight forward
 - Implementing counter was probably quicker than importing counter
 - .get(, default) is pretty easy to use
 - I feel like syntactic sugar in return basically sidesteps this whole quesiton, but :shrug:
 


"""
from typing import List
from unittest import TestCase

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        d = dict()

        for i in arr:
            d[i] = d.get(i, 0) + 1

        return len(d.keys()) == len(set(d.values()))

# Tests
tc = TestCase()
s = Solution()

tc.assertEqual(
    s.uniqueOccurrences(
       arr = [1,2,2,1,1,3]
    )
    , True
    )


tc.assertEqual(
    s.uniqueOccurrences(
        arr = [1,2]
    )
    , False
    )

tc.assertEqual(
    s.uniqueOccurrences(
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
    )
    , True
    )