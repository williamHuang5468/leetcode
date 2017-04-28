class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        row_size = len(board)
        col_size = len(board[0])
        shipList = []
        for y in range(len(board)):
            for x in range(len(board[y])):
                if (board[y][x] == "X") and ([x,y] not in shipList):
                    shipList.append([x,y])
                    count+=1
                    for row in range(x+1, col_size):
                        if board[y][row] =="X":
                            shipList.append([row,y])
                        else:
                            break
                    for col in range(y+1, row_size):
                        if board[col][x] =="X":
                            shipList.append([x,col])
                        else:
                            break
        return count
        
s = Solution()

board = [["X."], ["X."]]
assert s.countBattleships(board) == 1

board = [["X.."], ["..."]]
assert s.countBattleships(board) == 1

board = [["X.."], ["X.."]]
assert s.countBattleships(board) == 1

board = [["X.X"], ["X.."]]
assert s.countBattleships(board) == 2

board = [["X.X"],
         ["X.X"],
         ["..X"]]
assert s.countBattleships(board) == 2

board = [["X..X"],
         ["...X"],
         ["...X"]]
assert s.countBattleships(board) == 2

board = [["XX"],
         [".."]]
assert s.countBattleships(board) == 1
