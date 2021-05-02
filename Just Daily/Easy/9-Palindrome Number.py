# https://leetcode.com/problems/palindrome-number/solution/
# 16.83% speed, 92.24% memory
# HW: look at the algorithmic approach


import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #still gonna convert it to string
        x_str = str(x)
        #edge case: negative
        if x < 0:
            return False
        #edge case: ending with 0 (no number will start with 0xx)
        # if x_str[-1] == 0:
        #     return False
        #edge case: overflow
        if int(x_str[::-1]) > math.pow(2,31) - 1:
            return False
        return x_str == x_str[::-1]