"""

Start: 11:55
End: 11:48

https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75j

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000


Questions:
 - Response list ordering - doesn't matter

Options
 - Option 1: Brute force. Create sets s1 and s2. Loop through s1 and check for memebership in s2. Loop through s2 and check for membership in s1. Convert both to a list
   - T: O(max(n1, n2))
   - S: O(max(n1, n2))
   - Can we do better: Probably small optimizations, but probably not on time. Might be able to do better in space by manipulating input arrays, but this'd likely come at cost to time complexity

Edge cases

 - Empty lists

Notes

 - Started w/ 4 sets (set of each, return set of each). Could just compute the inersection and remove those - might be easier
 


"""
from typing import List
from unittest import TestCase

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        intersection = set()

        for i in s1:
            if i in s2:
                intersection.add(i)
        
        for i in intersection:
            s1.remove(i)
            s2.remove(i)

        return [list(s1), list(s2)]

# Tests
tc = TestCase()
s = Solution()

tc.assertEqual(
    s.findDifference(
        nums1 = [1,2,3], nums2 = [2,4,6]
    )
    , [[1,3],[4,6]]
    )


tc.assertEqual(
    s.findDifference(
        nums1 = [1,2,3,3], nums2 = [1,1,2,2]
    )
    , [[3],[]]
    )
