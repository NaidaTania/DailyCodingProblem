#https://leetcode.com/problems/decode-ways/discuss/30529/Readable-Python-DP-Solution


'''

For example:
s = "231"
index 0: extra base offset. dp[0] = 1
index 1: # of ways to parse "2" => dp[1] = 1
index 2: # of ways to parse "23" => "2" and "23", dp[2] = 2
index 3: # of ways to parse "231" => "2 3 1" and "23 1" => dp[3] = 2

'''

def numDecodings(s):
    if not s:
        return 0

    dp = [0 for x in range(len(s) + 1)]
    dp[0] = 1
    #set 2nd number as 1 if first number is not 0
    dp[1] = 1 if 0 < int(s[0]) <= 9 else 0
    print("Start:",dp)

    for i in range(2, len(s) + 1):
        if 0 < int(s[i-1]) <= 9:
            #if number is not zero, carry over previous number
            dp[i] += dp[i - 1]
            print(">>a",dp)
        #look at things 2 digit at a time
        #if first number != 0, and overall it's valid
        if s[i-2:i][0] != '0' and int(s[i-2:i]) <= 26:
            #add the value from 2 steps before
            #I don't get this part :(
            dp[i] += dp[i - 2]
            print(">>b",dp)
        print(dp)
    return dp[len(s)]

numDecodings("12211")
'''
1 -> 1 [1,1,0,0,0,0]
12 -> '1 2' and '12', [1,1,2,0,0,0]
122 -> '1 2 2', '12 2', '1 22', [1,1,2,3,0,0]
1221


'''