class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row and col check
        for i in range(len(board)):
            row = {}
            col = {}
            for j in range(len(board)):
                if board[i][j] != '.' and board[i][j] not in row:
                    row[board[i][j]] = 1
                elif board[i][j] != '.' and board[i][j] in row:
                    return False
                
                if board[j][i] != '.' and board[j][i] not in col:
                    col[board[j][i]] = 1
                elif board[j][i] != '.' and board[j][i] in col:
                    return False
        

        #sub_table check
        m1 = {}
        m2 = {}
        m3 = {}
        m4 = {}
        m5 = {}
        m6 = {}
        m7 = {}
        m8 = {}
        m9 = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if i in range(0,3) and j in range(0,3) and board[i][j] != '.':
                    try:
                        m1[board[i][j]] += 1
                        return False
                    except:
                        m1[board[i][j]] = 1
                
                elif i in range(0,3) and j in range(3,6) and board[i][j] != '.':
                    try:
                        m2[board[i][j]] += 1
                        return False
                    except:
                        m2[board[i][j]] = 1
                elif i in range(0,3) and j in range(6,9) and board[i][j] != '.':
                    try:
                        m3[board[i][j]] += 1
                        return False
                    except:
                        m3[board[i][j]] = 1

                elif i in range(3,6) and j in range(0,3) and board[i][j] != '.':
                    try:
                        m4[board[i][j]] += 1
                        return False
                    except:
                        m4[board[i][j]] = 1

                elif i in range(3,6) and j in range(3,6) and board[i][j] != '.':
                    try:
                        m5[board[i][j]] += 1
                        return False
                    except:
                        m5[board[i][j]] = 1
                
                elif i in range(3,6) and j in range(6,9) and board[i][j] != '.':
                    try:
                        m6[board[i][j]] += 1
                        return False
                    except:
                        m6[board[i][j]] = 1
                
                elif i in range(6,9) and j in range(0,3) and board[i][j] != '.':
                    try:
                        m7[board[i][j]] += 1
                        return False
                    except:
                        m7[board[i][j]] = 1
                elif i in range(6,9) and j in range(3,6) and board[i][j] != '.':
                    try:
                        m8[board[i][j]] += 1
                        return False
                    except:
                        m8[board[i][j]] = 1
                elif i in range(6,9) and j in range(6,9) and board[i][j] != '.':
                    try:
                        m9[board[i][j]] += 1
                        return False
                    except:
                        m9[board[i][j]] = 1

        return True
        
                



