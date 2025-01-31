"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
"""

class Solution:
    """
    Constraints: 
     - Input: candies - current amounts, extra candies - amount to give. 
     - Output: Array of len(candies), as to whether given extra candies the kid at that index would have the most
    Questions
     - >0 candies?
     - Fits within integer
     - Ties?
    Options
     - BF: For each kid, add and compare to all others. T: O(n2), S: O(n)
     - Sort: Create sorted array of (# candy, kid index). For each kid, add then compare to sorted list. T: O(nlgn), S: o(n)
       - Optimization: Do I need to sort the whole array? We only care about kids w/ between [max - amount to give, max] candy, as everyone else can't be topped over. This means they'll be false, and are not a contender for max after kid I is given extra candies
       - Optimization: Really the only contenders are the current max. Could I just compare kid i + extra to the current max?. T: O(n), S: o(n)
    """
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = candies[0]
        return_array = [False] * len(candies)
        for c in candies:
            if c > max_candies:
                max_candies = c
        
        for i, c in enumerate(candies):
            return_array[i] = c + extraCandies >= max_candies

        return return_array
    

s = Solution()
assert(s.kidsWithCandies([1,2,3], 1000) ==  [True, True, True])
assert(s.kidsWithCandies([1,2,2], 1000)== [True, True, True])
