# Question notes

## [1768_merge_strings_alternately](questions/1768_merge_strings_alternately.py)

Pretty straight forward. There is a slightly worse option (two pointers), but no better solution listed on leet code. 

Interestingly, leetcode doesn't consider the input strings or output string in the memory complexity

## [1071_greatest_common_divisor_of_strings](questions/1071_greatest_common_divisor_of_strings.py)]

No huge notes. I don't think I could have arrived at the math proof on my own, but it makes sense (and might be recognizable). 

Time to implement (31 minutes) is a little long, and implementation could have been cleaner.

## [1431_kids_with_the_greatest_number_of_candies](questions/1431_kids_with_the_greatest_number_of_candies.py)

No huge notes. Suprisingly straight forward - was it even worth mentioning BF / sorting options. 

Time to implement (10 minutes) is a little long. Also, couple of small implementation issues (e.g. calling to array instead of first element in array, clean variable names, python asserts don't really take 2 parameters but a `==` instead)

## [605_can_place_flowers](questions/605_can_place_flowers.py)

Time to implement (17 minutes) is a little long. Also, one minor implementation issue (originall `next <= len(flowerbed)` instead of `next >= len(flowerbed)`). The question was also a little unclear about whether the edge flower pots are fair game for planting, but it seems like they are. 

## [345_reverse_vowels_of_a_string](questions/345_reverse_vowels_of_a_string.py)

Pretty straight forward. All of the solutions are roughly the same time and space complexity, so I chose the one with the simplest code / most common data structures. Double pointer adds complexity, and stacks exist in python but are kind of uncommon.

Time to implement (10 minutes) was fine. First run didn't work because of an off by 1 error (using `len(vowels_found)` instead of `len(vowels_found) - 1`)

For reference:

 - A stack can be implemented w/ a append and pop usage of a normal list
 - The two pointer solution consumes less space, but is equal space complexity
