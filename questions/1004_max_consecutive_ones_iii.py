"""

Start: 1:13
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

 - It's tough to identify this as a sliding window problem. Once you've got it, its not too bad
 - Really getting stuck in random edge cases
 - Originally missed k=0 edge case
 - This feels like a failure, and super slow
 - Special cases for k=0 feel wonky. How could I handle them more gracefully or in the same logic as k > 0?
 - Mutation isn't actually necessary. Could just have a zeroes counter, and check while zeroes > k. Much cleaner


"""
from typing import List
from unittest import TestCase

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # print(nums, k)

        l = 0
        r = 0
        longest_ones = 0
        current_ones = 0
        remaining_flips = k
        sentinel_value = 2
        flipped_back_value = 3

        while r <= len(nums) - 1:
            # print(l, r, current_ones, nums)
            if nums[r] == 1:
                current_ones += 1
            
            # Current right value is 0, k=0
            elif k == 0:
                current_ones = 0
                l = r + 1
                

            # Current right value is 0, we can use a flip
            elif remaining_flips > 0:
                nums[r] = sentinel_value
                remaining_flips -= 1
                current_ones += 1

            # Current right value is 0, we cannot use a flip
            else:

                while remaining_flips == 0:
                    if nums[l] == sentinel_value:
                        nums[l] = flipped_back_value
                        remaining_flips += 1

                    current_ones -= 1
                    l += 1

                # Implement the flip
                nums[r] = sentinel_value
                remaining_flips -= 1
                current_ones += 1

            if current_ones > longest_ones:
                longest_ones = current_ones
            
            r += 1
        return longest_ones


tc = TestCase()
s = Solution()

tc.assertEqual(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2), 6)
tc.assertEqual(s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3), 10)
tc.assertEqual(s.longestOnes(nums = [0,0,1,1,1,0,0], k = 0), 3)
tc.assertEqual(s.longestOnes(nums = [0,0,0,0], k = 0), 0)
tc.assertEqual(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1], k = 0), 4)
