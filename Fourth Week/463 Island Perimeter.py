class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum([self.switchNumber(i) for i in self.countOne(grid)])
    
    ''' for loop version
    def countOne(self, grid):
        result = []
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                x_size = len(grid[y])
                y_size = len(grid)
                if grid[y][x] == 1:
                    if x != 0 and grid[y][x-1] == 1:
                        count +=1
                    if x+1 != x_size and grid[y][x+1] == 1:
                        count +=1
                    if y != 0 and grid[y-1][x] == 1:
                        count +=1
                    if y+1 != y_size and grid[y+1][x] == 1:
                        count +=1
                    result.append(count)
                    # reset
                    count = 0
        return result
    '''
    
    def countOne(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        return [self.countDirection(grid, x, y) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == 1]

    def countDirection(self, grid, x, y):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :rtype: List[int]
        """
        x_size = len(grid[y])
        y_size = len(grid)
        count = 0
        if x != 0 and grid[y][x-1] == 1:
            count +=1
        if x+1 != x_size and grid[y][x+1] == 1:
            count +=1
        if y != 0 and grid[y-1][x] == 1:
            count +=1
        if y+1 != y_size and grid[y+1][x] == 1:
            count +=1
        return count

        
    def switchNumber(self, num):
        switchDict = {4:0, 3:1, 2:2, 1:3, 0:4}
        return switchDict[num]
        
s = Solution()

#assert s.countOne([1]) == [0]
#assert s.countOne([1,1]) == [1,1]
assert s.countOne([[1,1],[1,0]]) == [2,1,1]
assert s.countOne([[1,1],[1,0],[1,0]]) == [2,1,2,1]

assert s.switchNumber(4) == 0
assert s.switchNumber(3) == 1
assert s.switchNumber(2) == 2
assert s.switchNumber(1) == 3
assert s.switchNumber(0) == 4

grid = [[1]]
assert s.islandPerimeter(grid) == 4

grid = [[1,1]]

assert s.islandPerimeter(grid) == 6
grid = [[1,1],
        [1,0]]
        
assert s.islandPerimeter(grid) == 8

grid = [[1,1],
        [1,1]]
assert s.islandPerimeter(grid) == 8

grid = [[1,1],
        [1,1],
        [1,0]]
assert s.islandPerimeter(grid) == 10

grid = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]

assert s.islandPerimeter(grid) == 16
