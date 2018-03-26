class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.values.append(x)
        if (len(self.min) == 0) or (x <= self.min[len(self.min)-1]) :
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.values.pop()
        if x == self.min[len(self.min)-1]:
            self.min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.values[len(self.values)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[len(self.min)-1]
