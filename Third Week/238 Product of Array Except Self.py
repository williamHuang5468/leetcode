class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1: return nums
        result = ([self.exceptNum(i,nums) for i in range(len(nums))])
        return [self.countIt(i) for i in result]
    
    def exceptNum(self, n, nums):
        return [nums[i] for i in range(len(nums)) if i != n ]
    
    def countIt(self, numList):
        n = 1
        for i in numList:
            n *= i
        return n
        
            


'''
Given an array of n integers where n > 1, nums,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Solve it without division and in O(n).
For example, given [1,2,3,4], return [24,12,8,6].

# Could you solve it with constant space complexity?
(Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''

s = Solution()
assert s.productExceptSelf([]) == []
assert s.productExceptSelf([2]) == [2]
assert s.productExceptSelf([1,2]) == [2,1]
assert s.productExceptSelf([1,2,3]) == [6,3,2]
assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert s.productExceptSelf([1,2,3,4,5]) == [120,60,40,30,24]
assert s.productExceptSelf([1,2,3,4,5,6]) == [720,360,240,180,144,120]

'''
len 2, [1], [0]
len 1, [0]
len 3, [1*2], [0*2], [0*1]
maybe can loop each elements when count is equal the i then pass it.
'''
