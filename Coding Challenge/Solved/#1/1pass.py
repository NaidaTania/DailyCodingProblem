'''
Attempt at one pass:
(sacrifice space)
1. make a hash table of num and diff
2. for each element, get diff value, check if value is in dict


space: O(n)
time: O(n)
'''


def checkAdd(int_list, sum):
    if len(int_list) == 0:
        return False
    elif len(int_list) == 1:
        if int_list[0] == sum:
            return True
        return False
    #one pass
    index = {}
    for key in int_list:
        #since we assume sum to be positive, can discard num > sum
        if key <= sum:
            index[key] = abs(sum-key)

    for key, diff in index.items():
        if diff in index.keys(): #this is O(1)
            return True
    return False



assert checkAdd([],0) == False
assert checkAdd([0],0) == True
assert checkAdd([1],0) == False
assert checkAdd([1,2,3,4],6) == True
assert checkAdd([0,2,3,4],4) == True