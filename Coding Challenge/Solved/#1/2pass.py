'''
Assumptions:
- int list
- return true if found, false otherwise
- sum is >= 0

Edge cases:
- list of 0 length
- list of 1 length


2 pass
- for each number, run another pass, check if added together = sum
space = O(1)
time = O(n^2)

'''


def checkAdd(int_list, sum):
    if len(int_list) == 0:
        return False
    elif len(int_list) == 1:
        if int_list[0] == sum:
            return True
        return False
    #double pass
    for i in range(len(int_list)):
        pivot = int_list[i]
        for j in range(i+1,len(int_list)):
            if pivot + int_list[j] == sum:
                return True
    return False



assert checkAdd([],0) == False
assert checkAdd([0],0) == True
assert checkAdd([1],0) == False
assert checkAdd([1,2,3,4],6) == True
assert checkAdd([0,2,3,4],4) == True
