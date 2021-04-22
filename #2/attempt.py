'''
My attempt, which works, but also time limit exceeded

time: O(n^2)
space: those 2 range lists there are O(n) :(

'''


def productExceptSelf(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return 

    returnarr = []
    for i in range(len(arr)):
        lower = list(range(0,i))
        upper = list(range(i+1,len(arr)))
        prod = 1
        for idx in lower + upper:
            prod *= arr[idx]
        returnarr.append(prod)
    return returnarr


assert productExceptSelf([10,20,30]) == [600,300,200]