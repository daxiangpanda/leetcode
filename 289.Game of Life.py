class Solution(object):
    # count the number of live cell
    def count(self,board,i,j):
        res = 0
        m = len(board)
        n = len(board[0])
        if i == 0:
            if j == 0:
                res = board[1][0]+board[1][1]+board[0][1]
            elif j == n-1:
                res = board[0][n-2]+board[1][n-2]+board[1][n-1]
            else:
                res = board[0][j-1]+board[1][j-1]+board[1][j]+board[1][j+1]+board[0][j+1]
        elif i == m-1:
            if j == 0:
                res = board[m-2][0]+board[m-2][1]+board[m-1][1]
            elif j == n-1:
                res = board[m-2][n-2]+board[m-1][n-2]+board[m-2][n-1]
            else:
                res = board[m-2][j-1]+board[m-1][j-1]+board[m-2][j]+board[m-2][j+1]+board[m-1][j+1]
        else:
            if j == 0:
                res = board[i-1][0]+board[i+1][1]+board[i-1][1]+board[i][1]+board[i+1][0]
            elif j == n-1:
                res = board[i-1][n-2]+board[i][n-2]+board[i+1][n-2]+board[i-1][n-1]+board[i+1][n-1]
            else:
                res = board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j-1]+board[i][j+1]+board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]
        return res

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 6 or board[i][j] == 7 or board[i][j] == 1 and self.count(board,i,j) < 2:
                    board[i][j] = 6
                elif (board[i][j] == 6 or board[i][j] == 7 or board[i][j] == 1) and (self.count(board,i,j) == 2 or self.count(board,i,j) == 3):
                    board[i][j] = 7
                elif (board[i][j] == 6 or board[i][j] == 7 or board[i][j] == 1) and self.count(board,i,j) > 3:
                    board[i][j] = 6
                elif (board[i][j] == 4 or board[i][j] == 5 or board[i][j] == 0) and self.count(board,i,j) == 3:
                    board[i][j] = 5
                else:
                    board[i][j] = 4
        # print board
        for i in range(m):
            for j in range(n):
                if board[i][j] == 4:
                    board[i][j] = 0
                elif board[i][j] == 5:
                    board[i][j] = 1
                elif board[i][j] == 6:
                    board[i][j] = 0
                elif board[i][j] == 7:
                    board[i][j] = 1
        # print board


a =Solution()
board = [[0,1,0],[1,1,0],[1,0,1]]
print board[0],board[0][1]
a.gameOfLife(board)