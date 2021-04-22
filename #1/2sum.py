#0.1MB better memory
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            raise Exception("Exactly 1 output is expected")
        index = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in index:
                return [i, index[diff]]
            index[nums[i]] = i #only adds to dict if value not found


#better timing by 24ms
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            raise Exception("Exactly 1 output is expected")
        index = {}
        for i in range(len(nums)):
            if nums[i] in index:
                #duplicate case would mean 2 same element
                #because 'exactly 1 solution'
                return [index[nums[i]],i]
            #num - index table
            index[nums[i]] = i
            diff = target-nums[i]
            if diff in index:
                if i is not index[diff]:
                    return [i, index[diff]]
