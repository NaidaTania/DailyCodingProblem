'''
With division:
- check total 0s, get all num multiplied
- if >2 0s, return all 0s
- if not, return an arr of total divided by the number in that position
- if there is a single 0, replace position of index of 0 with total

Without division:

'''


# from operator import mul

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         total = 1
#         zeros = 0
        
#         for i in nums:
#             if i == 0:
#                 zeros += 1 #count number of 0s
#             else:
#                 total = total * i #multiply everything
        
#         if zeros == 0:
#             return [total // i for i in nums]
        
#         elif zeros > 1:
#             return [0 for i in nums] #if there is 0, forget it
        
#         else:
#             output = [0 for i in nums]
#             i = nums.index(0)
#             nums.pop(i)
#             output[i] = reduce(mul, nums, 1)
#             return output



class Solution2:
    def productExceptSelf(self, nums):
        """
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        # n = len(nums)
        # # l[i]: product up to i (exluded)
        # l = [1] * n #[1 1 1 1 1]
        # # r[i]: product start from i (exluded)
        # r = [1] * n #[1 1 1 1 1]
        
        # #what the heck is happening here
        # # [1 1 1 1 1] 
        # # [1 2 3 4 5]
        # for i in range(1, n):
        #     print("l[{}] = {} * {} = {}".format(i,l[i-1],nums[i-1], l[i - 1] * nums[i - 1]))
        #     l[i] = l[i - 1] * nums[i - 1]
        # print("l is", l)
        # print("looping from range {} to {} backwards".format(n-2,-1))
        # for i in range(n - 2, -1, -1):
        #     print("r[{}] = {} * {} = {}".format(i,r[i+1],nums[i+1], r[i + 1] * nums[i + 1]))
        #     r[i] = r[i + 1] * nums[i + 1]
        # print("r is", r)
        # ans = [l[i] * r[i] for i in range(n)]

        # return ans
        
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        Intuition:
            Update ith and n - i - 1 position in the ans at the same time.


            When i iterate before the half of nums,    
            ans[i] and ans[n - 1 - i] just store the 
            left product before i and right product after i, 
            however when i iterate after the half of the nums, since
            nums[i] keep the right product before, l * nums[i] will be the left product * right prodcut
            so does nums[n - 1 - i] * r.
        """
        n = len(nums)
        ans = [1] * n
        
        #Keep store the left product and right product of i as l and r.
        l, r = 1, 1
        
        for i in range(n):
            ans[i] *= l
            print("ans [{}] *= {}".format(i,l))
            print(ans)
            ans[n - 1 - i] *= r
            print("ans [{}] *= {}".format(n - 1 - i,r))
            print(ans)
            
            print("l *= {} -> {} *= {} = {}".format(nums[i],l,nums[i],l*nums[i]))
            l *= nums[i]
            print("r *= {} -> {} *= {} = {}".format(nums[n-1-i],r,nums[n-1-i],r*nums[n-1-i]))
            r *= nums[n - 1 - i]
        return ans


s2 = Solution2()
s2.productExceptSelf([1,2,3,4,5])