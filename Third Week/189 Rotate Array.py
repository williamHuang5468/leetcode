'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size is not 0 and k is not 0:
            offset = k % size
            nums = nums[size-offset:] + nums[:size-offset]
        return nums
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size is not 0 and k is not 0:
            offset = k % size
            right = [nums[i] for i in range(size-offset)]
            left = [nums[i] for i in range(size-offset, size)]
            return left + right
        return nums

'''
Probility situation
1. nums_len = k
2. nums_len > k
3. nums_len < k
'''
s = Solution()
assert s.rotate([], 0) == []
assert s.rotate([2], 0) == [2]
assert s.rotate([2], 1) == [2]
assert s.rotate([2], 2) == [2]
assert s.rotate([2], 3) == [2]
assert s.rotate([1, 2], 1) == [2, 1]
assert s.rotate([1, 2], 2) == [1, 2]
assert s.rotate([1, 2, 3], 1) == [3, 1, 2]
assert s.rotate([1, 2, 3], 2) == [2, 3, 1]
assert s.rotate([1, 2, 3], 3) == [1, 2, 3]
# n < k
assert s.rotate([1, 2, 3], 4) == [3, 1, 2]
assert s.rotate([1, 2, 3], 5) == [2, 3, 1]
assert s.rotate([1, 2, 3], 6) == [1, 2, 3]
assert s.rotate([1, 2, 3, 4], 1) == [4, 1, 2, 3]
assert s.rotate([1, 2, 3, 4], 2) == [3, 4, 1, 2]
assert s.rotate([1, 2, 3, 4], 3) == [2, 3, 4, 1]
assert s.rotate([1, 2, 3, 4], 4) == [1, 2, 3, 4]
assert s.rotate([1, 2, 3, 4], 5) == [4, 1, 2, 3]
assert s.rotate([1, 2, 3, 4], 6) == [3, 4, 1, 2]
assert s.rotate([1, 2, 3, 4], 7) == [2, 3, 4, 1]
assert s.rotate([1, 2, 3, 4], 8) == [1, 2, 3, 4]
