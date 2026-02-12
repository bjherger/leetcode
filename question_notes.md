# Question notes

Working through [Leetcode 75](https://leetcode.com/studyplan/leetcode-75/)

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

## [151_reverse_words_in_a_string](questions/151_reverse_words_in_a_string.py)

Time to implement (7 minutes) was fine. First run didn't work because of a mistake in the final flush after the for loop (using `word_list.append(word_buffer)` instead of `word_list.append(''.join(word_buffer))`). Second run had errors, due to spaces being included. Fixed by separating `if c == ' ' and len(word_buffer) > 0:` into two separate if statements.

## [227_basic_calculator_ii](questions/227_basic_calculator_ii.py)

Non-leetcode 75 special side treck

Took 55 minutes and some peeking at a chat GPT solution to answer. I would not have arrived at using a stack on my own, and the solution was pretty tricky. This is a pretty hard question. I should practice it again, given that it seems to come up often.

My intuition is not to use a stack, but to use a recursive approach, but this would be pretty thorny (subbing in multiplication results)

## [238_product_of_array_except_self.py](questions/238_product_of_array_except_self.py)

This one is just about getting the prefix / suffix trick

 - Originally had prefix, suffix and result
 - Combined prefix and result pass, removed prefix array

Follow up (O(1) except for return array)
This is tough. Easy to do in T: O(N^2). Complex data type for storing suffix in result array.

Oh, we can just populate the result array with the suffix value at each position. It's no longer needed after we compute position i

### Chat GPT feedback

 - Could have avoided reversed by just iterating backwards w/o extra list
 - Initializing w/ None is fine, could have inited w/ ints

## [334_increasing_triplet_subsequence.py](questions/334_increasing_triplet_subsequence.py)

Started w/ option 2 (array of indicies sorted by value). This is complicated and breaks. It breaks because
 - Duplicates
 - ie 0, 5, 2, 3 would be hard / require back tracking

There is a much easier O(N). Just track smallest and second smallest seen. 

Implemention option 4

 - Initializing smallest and second smallest is important. Can't just initialize w/ first few values (e.g. index 1 is smaller than index 0). Setting to a large value seems to work
 - I've implemented it, but I'm not entirely sure why this works?
 - Ties kind of matter
 - It's easier to just use a quick check to see if the current value is equivalent to either smallest or second smallest. If so, we can just continue
 - Leetcode is showing a really long run time relative to others (?). Oh, this is just due to print statement
