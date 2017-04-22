'''
法一
使用 build-in，去排序 dictiionary
'''
'''
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
        result = self.orderValue(numberDict)
        return [result[i][0] for i in range(k)]
    def orderValue(self, dict):
        from operator import itemgetter
        return sorted(dict.items(), key=itemgetter(1), reverse=True)
'''
'''
法二
直接使用相關 lib
class Solution(object):
    def topKFrequent(self, nums, k):
        from collections import Counter
        result = Counter(nums).most_common(k)
        return [result[i][0] for i in range(k)][::-1]
'''
'''
暴力解，超 慢 ~ 待改善
'''
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
        sortDict = sorted(numberDict.values(), reverse= True)
        result = []
        for i in range(k):
            for key,value in numberDict.items():
                if value is sortDict[i] and key not in result:
                    result.append(key)
                    break
        return result[::-1]

s = Solution()

assert s.topKFrequent([1,2], 2) == [1,2]
assert s.topKFrequent([1,1,2], 1) == [1]
assert s.topKFrequent([1,1,2], 2) == [1,2]
assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert s.topKFrequent([4,1,-1,2,-1,2,3], 2) == [-1,2]
