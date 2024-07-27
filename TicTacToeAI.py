class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A 3x3 board represented as a list of 9 elements
        self.current_player = 'X'  # 'X' starts the game

    def print_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("---------")

    def is_winner(self, player):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)               # Diagonals
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def is_draw(self):
        return all(cell != ' ' for cell in self.board) and not (self.is_winner('X') or self.is_winner('O'))

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_draw()

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def get_available_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == ' ']

def minimax(board, depth, is_maximizing):
    if board.is_winner('X'):
        return -10 + depth
    elif board.is_winner('O'):
        return 10 - depth
    elif board.is_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in board.get_available_moves():
            board.make_move(move, 'O')
            score = minimax(board, depth + 1, False)
            board.board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in board.get_available_moves():
            board.make_move(move, 'X')
            score = minimax(board, depth + 1, True)
            board.board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_move = None
    best_score = -float('inf')
    for move in board.get_available_moves():
        board.make_move(move, 'O')
        score = minimax(board, 0, False)
        board.board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def minimax_with_alpha_beta(board, depth, alpha, beta, is_maximizing):
    if board.is_winner('X'):
        return -10 + depth
    elif board.is_winner('O'):
        return 10 - depth
    elif board.is_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in board.get_available_moves():
            board.make_move(move, 'O')
            score = minimax_with_alpha_beta(board, depth + 1, alpha, beta, False)
            board.board[move] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for move in board.get_available_moves():
            board.make_move(move, 'X')
            score = minimax_with_alpha_beta(board, depth + 1, alpha, beta, True)
            board.board[move] = ' '
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

def find_best_move_with_alpha_beta(board):
    best_move = None
    best_score = -float('inf')
    alpha = -float('inf')
    beta = float('inf')
    for move in board.get_available_moves():
        board.make_move(move, 'O')
        score = minimax_with_alpha_beta(board, 0, alpha, beta, False)
        board.board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    game = TicTacToe()
    while not game.is_game_over():
        game.print_board()
        if game.current_player == 'X':
            position = int(input("Enter your move (0-8): "))
            if not game.make_move(position, 'X'):
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is making a move...")
            position = find_best_move_with_alpha_beta(game)
            game.make_move(position, 'O')
        game.current_player = 'O' if game.current_player == 'X' else 'X'

    game.print_board()
    if game.is_winner('X'):
        print("You win!")
    elif game.is_winner('O'):
        print("AI wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
