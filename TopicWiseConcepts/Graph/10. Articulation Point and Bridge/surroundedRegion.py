
### https://leetcode.com/problems/surrounded-regions/description/ ##

from collections import deque
class Solution(object):
    def isValid(self, i , j, board):
        m = len(board)
        n = len(board[0])
        if i >= 0 and i < m and j >=0 and j < n and board[i][j] == "O":
            return True
        return False

    def DFS(self, board, i, j):
        que = []
        que.append([i,j])
        while que:
            curr = que.pop()
            board[curr[0]][curr[1]] = "T"
            if self.isValid(curr[0]+1, curr[1], board):
                que.append((curr[0]+1, curr[1]))
            if self.isValid(curr[0]-1, curr[1], board):
                que.append((curr[0]-1, curr[1]))
            if self.isValid(curr[0], curr[1]+1, board):
                que.append((curr[0], curr[1]+1))
            if self.isValid(curr[0], curr[1]-1, board):
                que.append((curr[0], curr[1]-1))


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """        
        
        m = len(board)
        n = len(board[0])

        for i in range(m):
            if board[i][0] == "O":
                self.DFS(board, i, 0)
            if board[i][n-1] == "O":
                self.DFS(board, i, n-1)           

        for j in range(n):
            if board[0][j] == "O":
                self.DFS(board, 0, j)
            if board[m-1][j] == "O":
                self.DFS(board, m-1, j)   

        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"

        return board