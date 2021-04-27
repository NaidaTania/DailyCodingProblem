'''
Given 111
it can be aaa (1,1,1)
or ka (11,1)
or ak (1,11)

ambiguity happens with 1_(10 to 19) and 2_(20 to 26)
any number other than 1 and 2 does not result in ambiguity

A brute force attempt that does not consider algorithmic approach xD
(yep this is definitely not the way to approach it.)
'''

def decodeWays(msg):
    if msg[0] == '0':
        return 0
    vocab = dict((i, chr(64+i)) for i in range(1,27))
    # print(vocab)
    total = 0
    prev = False
    prevone = False
    prevtwo = False
    repeat = 0
    plain = False
    ten = False
    for digit in msg:
        print("digit:",digit)
        if digit in ['1','2']:
            repeat += 1
            if prev:
                print("+1 bc prev")
                total += 1
                continue
            if digit == '1':
                prevone = True
            else:
                prevtwo = True
            print("+1 bc 1/2")
            total += 1
            prev = True
        # print("+1 per every number?")
        else:
            if (digit == '0' and prevone):
                print("no add since 10")
                #the 1 in 10 is always counted as 1 already
                # total -= 1
                prevone = False
                ten = True
            elif (int(digit)>6 and prevtwo):
                print("no add since >26")
                # total -= 1
                prevtwo = False
            else:
                if repeat <= 2 and plain:
                    print("-",repeat-1,"for repeat grace")
                    total -= (repeat - 1)
                    plain = False
                else:
                    print("+1 plain non 1/2")
                    plain = True
                    total += 1
            prev = False
            repeat = 0
            #wait, each repeated occurence means + 1
    print("total:",total)
    return total


assert decodeWays("111") == 3
assert decodeWays("12") == 2
assert decodeWays("226") == 3
assert decodeWays("227") == 2 #2 2 7; 22 7 
assert decodeWays("0") == 0
assert decodeWays("06") == 0 
assert decodeWays("1213") == 4
assert decodeWays("10") == 1
assert decodeWays("1010") == 2
assert decodeWays("911") == 2 #9 1 1; 9 11 died here
assert decodeWays("1011") == 2 #and here
'''
if we rethink it as it can decode at most as much letter as itself
and then for every 10-19, 20-26, we minus 1 
'''