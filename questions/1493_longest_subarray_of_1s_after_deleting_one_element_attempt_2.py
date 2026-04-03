"""
Start: 15:52
End: 15:57

https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.
Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:

- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.

Questions / notes:
 - Must delete? Yes
 - Empty array? Wont happen
 - No 1s? Return 0
 - Need position of longest 1s / index? No

Options
 - O1: Brute force. Skip / pretend to remove each element, compute longest array of 1s
   - T: O(n2)
   - S: O(1) (can keep index of skip)
 - O2: Sliding window of 1s. Track window start, skip element, current index
   - T: O(n)
   - S: O(1)
   - Can we do better? No need to touch every element

Notes for next time:
 - Edge case for Current span is all ones, but we can delete a zero somewhere else
 - Writing a compute span function is helpful
 - Using an initialize loop is also helpful. It's nice to have different logic for if there is a deleted 0 or not already
"""

from typing import List
from unittest import TestCase, skip

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        best = 0
        right = 0
        zeros = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left)
            right += 1
        return best


tc = TestCase()
tc.assertEqual(Solution().longestSubarray([1, 1, 0, 1]), 3)
tc.assertEqual(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5)
tc.assertEqual(Solution().longestSubarray([1, 1, 1]), 2)
tc.assertEqual(Solution().longestSubarray([0, 0, 1, 1]), 2)
tc.assertEqual(Solution().longestSubarray([0, 0]), 0)
