#largest sum of non adjacent number

'''
Ignoring best constraint, let's arrive at a solution

For example, [2, 4, 6, 2, 5] should return 13, 
since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Approach:
Save top greatest 4 numbers and its index
(I misread the qn and only summed 2 numbers rather than all possible ones oops.)
'''

import sys

def updateTop4(i, n, top4, top4idx):
    for idx, num in enumerate(top4):
        if n > num:
            top4[idx] = n
            top4idx[idx] = i
            break
    return top4, top4idx


def sumNonAdj(nums):
    top4 = [0,0,0,0]
    top4idx = [0,0,0,0]
    for i, n in enumerate(nums):
        # print(i,n)
        top4, top4idx = updateTop4(i, n, top4, top4idx)
    total = -1 * sys.maxsize
    for i, t in enumerate(top4):
        for j in range(i,len(top4)):
            local_total = t + top4[j]
            diff = abs(top4idx[i] - top4idx[j])
            if local_total > total and diff > 1:
                print("?")
                total = local_total
    print("top4:",top4)
    print("idxs:",top4idx)
    print("total:",total)
    return total

sumNonAdj([2, 4, 6, 2, 5])
sumNonAdj([5, 1, 1, 5] )