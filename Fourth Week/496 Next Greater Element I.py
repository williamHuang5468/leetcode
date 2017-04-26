'''
Stack + Dict
建表，不在表中的就 -1
'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        letterDict = {}
        stack = []
        for item in nums:
            while(len(stack) and stack[-1] < item):
                letterDict[stack.pop()] = item
            stack.append(item)
        return [letterDict.get(i, -1) for i in findNums]
                
'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        return [self.walkRoundNums(item, nums) for item in findNums]
    
    def walkRoundNums(self, item, nums):
        try:
            index = nums.index(item)
            return self.findGreater(nums, index, item)
        except ValueError:
            return -1

    def findGreater(self, nums, j, i):
        for index in range(j, len(nums)):
            if nums[index] > i:
                return nums[index]
        return -1
'''
'''
暴力法
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        result = []
        for i in findNums:
            for j in range(len(nums)):
                if i == nums[j]:
                    if nums[j] != nums[-1]:
                        j+=1
                        result.append(self.findGreater(nums, j, i))
                        break
                    else:
                        result.append(-1)
                        break
            else:
                result.append(-1)
        return result
    def findGreater(self, nums, j, i):
        for index in range(j, len(nums)):
            if nums[index] > i:
                return nums[index]
        return -1
'''
    
# Thinking
'''
- find the element of findNums on nums
- if find it
    - check is last one on nums then given -1.
    - check the next one is greater.
- if not found, given -1.
'''

s = Solution()
assert s.nextGreaterElement([1], [1,2]) == [2]
assert s.nextGreaterElement([1], [1]) == [-1]
assert s.nextGreaterElement([1], [2]) == [-1]
assert s.nextGreaterElement([4,1], [1,4]) == [-1, 4]

##
assert s.nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
assert s.nextGreaterElement([2,4], [1,2,3,4]) == [3,-1]
assert s.nextGreaterElement([2,3], [3,2,1,5]) == [5,5]
assert s.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]) == [7,7,7,7,7]
assert s.nextGreaterElement([137,59,92,122,52,131], [137,59,92,122,52,131]) == [-1,92,122,131,131,-1]
