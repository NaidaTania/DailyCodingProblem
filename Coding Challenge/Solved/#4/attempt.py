'''
Probably not O(n) time and O(1) space quite yet
But an attempt at a solution:
time: O(n)
space: also O(n)

So if 1 exist, answer is not 1
if all the number have no gap, answer is max + 1
if there is a gap somewhere in the answer, answer is the gap of the smallest numbers

'''

import sys

def firstSmallestPositive(nums):
    num_dict = {} #the numbers, and the number that is supposed to be right after it
    #also keep track of max
    max_num = -1
    found_one = False
    for n in nums:
        #keep track of max
        if n > max_num:
            max_num = n
        #ignore negative
        if n >= 0 and n not in num_dict:
            num_dict[n] = n + 1
        if n == 1:
            found_one = True
    #no found 1
    if found_one == False:
        return 1
    min_gap = sys.maxsize
    for v in  num_dict.values():
        if v not in num_dict and v < min_gap:
            min_gap = v-1 #add the key in
    if min_gap == sys.maxsize:
        return max_num + 1
    return min_gap + 1
    #check if there is 1. if no 1, return 1
    #then from num_dict's values, check if it exist. If not, keep it
    #but when keeping, only keep the minimum one
    #if no gap, return max+1

assert firstSmallestPositive([3, 4, -1, 1]) == 2
assert firstSmallestPositive([1, 2, 0]) == 3
assert firstSmallestPositive([7,8,9,11,12]) == 1