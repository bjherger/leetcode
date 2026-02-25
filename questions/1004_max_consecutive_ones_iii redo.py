"""

Start: 10:55
End: 2:14

https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Questions

 - Don't need to return position of 0's flipped, or range of 1s
 - No limit on distribution of 0s
 - k <= n
 - Max array can be longer than k


Options
 - Option 1: Brute force. Try all permutations, filter to those with at most k flipped, find the max consecutive range of 1s
   - T: O(2^n)
   - S: O(2^n)
 - Option 2: Slightly less brute force. Only flip up to k
   - T: O(2^k)
   - S: O(2^k)
   - Can we do better? Very likely
 - Option 3: Sliding window. Track longest seen, and remaining flips. Roll window through one position at a time. If right is zero, use a flip if remaining, or move window to the right until a flip becomes available. If right is 1 increment current max length. If max length exceeds, set to new max mangth. Use sentinel value to denote flipped?
   - T: O(n)
   - S: O(1) (if can modify in place)

Edge cases

 - L surpasses R. K can be 0, so they can be the same

Notes

 - Trying again. I was unhappy with the solution complexity before. I think the trick is really the way that zero counts are registered


"""
from typing import List
from unittest import TestCase

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        num_ones = 0
        num_zeroes = 0
        l = 0
        r = 0

        while r <= len(nums) - 1:
            if nums[r] == 1:
                num_ones += 1
            elif num_zeroes < k:
                num_ones += 1
                num_zeroes += 1
            else:
                while num_zeroes == k:
                    if nums[l] == 0:
                        num_zeroes -= 1
                    num_ones -= 1
                    l += 1

                num_ones += 1
                num_zeroes += 1

            if num_ones > max_ones:
                max_ones = num_ones

            r += 1

        return max_ones


tc = TestCase()
s = Solution()

tc.assertEqual(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2), 6)
tc.assertEqual(s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3), 10)
tc.assertEqual(s.longestOnes(nums = [0,0,1,1,1,0,0], k = 0), 3)
tc.assertEqual(s.longestOnes(nums = [0,0,0,0], k = 0), 0)
tc.assertEqual(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1], k = 0), 4)
