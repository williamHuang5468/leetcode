class Stock(object):
    def maxProfit(self, prices):
        '''
        First Solution : brute force 
            use O(nLogn) to find the soluition
        Second Solution : find the pattern
            find the pattern, the maxProfit is the ith behind max value.
            it is mean I need to find the min value and after the value to find the max value.
            And to get the max offset.
        e.g. [1,2,3,4]
        All
        0,1
        0,2
        0,3
        1,2
        1,3
        2,3

        Just 0 max[1,2,3]
        Just 1 max[2,3]
        Just 2 max[3]
        '''
        profit = 0
        size = len(prices)
        for i in range(size):
            startValue = prices[i]
            for j in range(i+1, size):
                endValue = prices[j]
                if(endValue <= startValue):
                    continue
                offset = endValue - startValue
                profit = max(profit, offset)
        return profit