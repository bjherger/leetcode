"""

Start: 1:20
End: 1:39

https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 10**4
-2**31 <= nums[i] <= 2**31 - 1
 

Follow up: Could you minimize the total number of operations done?

Questions: 

 - Duplicate zeros: OK, will happen
 - Data range: given

Options:

 - Option 1: Brute force, every time a zero is encountered move all elements up one and pad a zero to the end
   - T: O(N^2)
   - S: O(1) (original array modified)
 - Option 2: Two pointers - one at current write head, another at current read head. When read head reaches the end, pad out w/ zeros
   - T: O(N)
   - S: O(1) (original array modified)

"""
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_index = 0
        read_index = 0
        skip_value = 0

        while read_index +1 <= len(nums):
            value = nums[read_index]

            if value != skip_value:
                nums[write_index] = value
                write_index += 1
                read_index += 1
            else:
                read_index += 1
        
        while write_index + 1 <= len(nums):
            nums[write_index] = 0
            write_index += 1
        
s = Solution()

assert(s.moveZeroes([1,2,3,4,5]) == None)

a = [0, 0, 0]
s.moveZeroes(a)
assert(a == [0, 0, 0])

a = [0, 1, 0]
s.moveZeroes(a)
assert(a == [1, 0, 0])

a = [1, 1, 1]
s.moveZeroes(a)
assert(a == [1, 1, 1])

a = [0,1,0,3,12]
s.moveZeroes(a)
assert(a == [1,3,12,0,0])
