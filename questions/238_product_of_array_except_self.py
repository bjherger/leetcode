"""

Start: 3:23
End: 3:45 (default)
End: TODO (Follow up)

https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
Requirements
 
Questions
 - Number range: -30 to 3-
 - Negatives: YEs
 - Zero: Yes

Options
 - Option 1: Brute force: For each index, multiply other elements. T: O(n^2), S: O(1) (not counting output array)
 - Option 2: Prefixes and suffixes. T: O(n), S: O(N) (intermediate array)
   - Can we do better? Not for time, we need at least T: O(N) to traverse. Maybe on space
 - Option 3: Prefixes and suffixes. T: O(n), S: O(1) (Use return array to hold data. This feels like a very rough defintion of space complexity thoguh)

"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [None] * len(nums)
        result = [None] * len(nums)

        # Backwards pass for suffix
        suffix_agg = 1
        for (i, num_value) in reversed(list(enumerate(nums))):
            suffix[i] = suffix_agg
            suffix_agg *= num_value


        # Forward pass for prefix, result
        prefix_agg = 1
        for (i, num_value) in enumerate(nums):
            result[i] = prefix_agg * suffix[i]
            prefix_agg *= num_value
        
        return result
        
    
s = Solution()
print(s.productExceptSelf([-1,1,0,-3,3]))
assert(s.productExceptSelf([1,2,3,4]) == [24, 12, 8, 6])
assert(s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])