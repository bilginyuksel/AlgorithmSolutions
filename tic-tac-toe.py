class TicTacToe:
    def _display(self, board):
        for i in range(3):
            for j in range(3):
                print(board[i][j], end=' ')
            print()

    def _initBoard(self):
        return [['-' for _ in range(3)] for _ in range(3)]

    def _nextTurn(self, player):
        return 'o' if player=='x' else 'x'

    def _humanMove(self, board, player):
        x, y = self._getInput()
        if x is None or y is None: return player

        if board[x][y] == '-':
            board[x][y] = player 
            return self._nextTurn(player) 

        print("you can't move to cell (%d,%d)" % (x, y))
        return player

    def _move(self, board, turn):
        return self._humanMove(board, turn)

    def _getInput(self):
        #try:
        x, y = map(int, input().split())
        return x, y
        #except:
        #    print('wrong input format! it should be space seperated 2 integers. (1 2)')
        #    return None, None

    def _getGameStatus(self, board):
        current, end = None, False
        # vertical, horizontal check
        for i in range(3):
            currentHorizontal = board[i][0]
            currentVertical = board[0][i]
            endHorizontal = endVertical = True
            for j in range(3):
                if currentHorizontal != board[i][j]: 
                    endHorizontal = False
                if currentVertical != board[j][i]:
                    endVertical = False

            if currentHorizontal != '-' and endHorizontal:
                return currentHorizontal, True
            if currentVertical != '-' and endVertical:
                return currentVertical, True

        # diagonal check
        isDiagonalLTR = True
        for i,j in zip(range(1,3), range(1,3)):
            if board[i][j] != board[i-1][j-1] or (board[i][j] == board[i-1][j-1] and board[i][j]=='-'):
                isDiagonalLTR = False
                break
        if isDiagonalLTR: return board[0][0], True

        isDiagonalRTL = True
        for i,j in zip(range(1,3), range(1,-1, -1)):
            if board[i][j] != board[i-1][j+1] or (board[i][j] == board[i-1][j+1] and board[i][j]=='-'): 
                isDiagonalRTL = False
                break
        if isDiagonalRTL: return board[0][-1], True

        emptyCells = sum(row.count('-') for row in board) 
        return None, emptyCells == 0

    def start(self):
        board = self._initBoard()
        turn = 'x' # x means human o means computer
        winner, isEnd = None, False
        self._display(board)
        while not isEnd:
            turn = self._move(board, turn)
            winner, isEnd = self._getGameStatus(board)
            self._display(board)

        print('Draw!' if winner is None else winner)
        return winner

class TicTacToeComputer(TicTacToe):

    def _findMinMaxScore(self, board, turn, player):
        winner, end = self._getGameStatus(board)
        if end and winner is None:
            return 0
        elif end and winner == player:
            return 10
        elif end and winner != player:
            return -10

        score = 0 
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = turn
                    score += self._findMinMaxScore(board, self._nextTurn(turn), player)
                    board[i][j] = '-' 
        return score


    def _computerMove(self, board, player):
        bestScore = float('-inf')
        bestPosition = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    # is this the best move check
                    board[i][j] = player;
                    score = self._findMinMaxScore(board, player, player)
                    if score > bestScore:
                        bestScore = score
                        bestPosition = [i,j]

                    board[i][j] = '-';

        x, y = bestPosition
        board[x][y] = player
        return self._nextTurn(player)

                    


    def _move(self, board, turn):
        if turn == 'x':
            return self._humanMove(board, turn) 
        return self._computerMove(board, turn)

game = TicTacToeComputer()
game.start()

