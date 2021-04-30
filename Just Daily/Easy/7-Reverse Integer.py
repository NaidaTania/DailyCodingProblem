# 86.64% speed, 11.24% memory
# https://leetcode.com/problems/reverse-integer/

import math

class Solution:
    def reverse(self, x: int) -> int:
        max_num = math.pow(2,31) - 1
        min_num = math.pow(2,31) * -1
        if x < 0:
            return_val = int(str(x)[:0:-1]) * -1
        else: 
            return_val = int(str(x)[::-1])
        if return_val <= min_num or return_val >= max_num:
            return 0
        return return_val
        