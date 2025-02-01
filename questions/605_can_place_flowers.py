"""
https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Constraints
Questions
 - Does ..., 0,1] fulfill the requirement?
 - Existing state - any that currently violate this requirement?

Options
 - BF: Sliding window. T: O(n), S: O(1)
 - Can we do better? No, probably not
 - Optimization: Stop when we reach n

 Examples
 [1, 1] -> no new flowers
 [0, 0] -> 1 new flower
 [1, 0, 0, 0, 1] -> 1 new flower
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for current in range(len(flowerbed)):
            previous = current - 1
            next = current+1

            if (previous < 0 or flowerbed[previous] == 0) \
                    and (flowerbed[current] == 0) \
                    and (next >= len(flowerbed) or flowerbed[next] == 0):
                n -= 1
                flowerbed[current] = 1
            if n <= 0:
                return True
        return False
        pass

s = Solution()

assert(s.canPlaceFlowers([0, 0, 0], 1) == True)
assert(s.canPlaceFlowers([1, 1, 1], 1) == False)
assert(s.canPlaceFlowers([1,0,0,0,0,1], 2) == False)