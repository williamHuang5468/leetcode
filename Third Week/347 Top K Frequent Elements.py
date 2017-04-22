class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numberDict = {}
        for i in nums:
            if i not in numberDict:
                numberDict[i] = 1
            else:
                numberDict[i] +=1
        print(numberDict.values())

s = Solution()
assert s.topKFrequent([1,1,2], 1) == [1,2]
assert s.topKFrequent([1,1,2], 2) == [1]

# TODO....
