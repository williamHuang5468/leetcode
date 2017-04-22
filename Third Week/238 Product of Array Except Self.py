'''
方法一，暴力解，O(n^2)


1. 組合排除特定元素的 List
2. 相乘

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1: return nums
        result = []
        n = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    n *= nums[j]
            result.append(n)
            n = 1
        return result
'''

'''
法二，先乘，然後用除法
除 0 另外處理
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        if size == 1: return nums
        countZero = nums.count(0)
        if countZero > 1:
            return [0] * size
        elif countZero == 1:
            multiplyResult = self.multiplyOtherNumber(nums)
            return [multiplyResult if nums[i] == 0 else 0 for i in range(size)]
        else:
            multiplyResult = self.multiplyOtherNumber(nums)
            return [multiplyResult / nums[i] for i in range(size)]

    def multiplyOtherNumber(self, numList):
        n = 1
        for i in numList:
            if i != 0:
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

# 單個 0 的 case
assert s.productExceptSelf([0]) == [0]
assert s.productExceptSelf([0,1]) == [1,0]
assert s.productExceptSelf([0,1,2]) == [2,0,0]
assert s.productExceptSelf([0,1,2,3]) == [6,0,0,0]
# 兩個 0 的 case
assert s.productExceptSelf([0,1,0,3]) == [0,0,0,0]
assert s.productExceptSelf([0,0]) == [0,0] 
'''
len 2, [1], [0]
len 1, [0]
len 3, [1*2], [0*2], [0*1]
maybe can loop each elements when count is equal the i then pass it.
'''
