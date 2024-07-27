Tic-Tac-Toe AI
<br>This project implements a Tic-Tac-Toe game where a human player can play against an AI. The AI is built using the Minimax algorithm with optional Alpha-Beta Pruning to ensure optimal performance and make the AI as challenging as possible.

<br>Features
<br>Classic Tic-Tac-Toe Game: Play the traditional game of Tic-Tac-Toe with a 3x3 grid.
<br>Human vs. AI: Compete against an AI opponent that uses Minimax or Alpha-Beta Pruning to make the best moves.
<br>Optimal Play: The AI is designed to be nearly unbeatable by evaluating all possible moves and outcomes.

<br>How to Play
<br>The game starts with an empty board.
<br>The human player (X) is prompted to enter their move by specifying a position between 0 and 8.
<br>After the human player's move, the AI (O) calculates and makes its move.
<br>The game continues until there is a winner or the board is full (resulting in a draw).
<br>The final result of the game is displayed: either "You win!", "AI wins!", or "It's a draw!".

<br>Code Explanation
<br>TicTacToe Class
<br>__init__(): Initializes the game board and sets the starting player.
<br>print_board(): Displays the current state of the board.
<br>is_winner(player): Checks if the specified player has won the game.
<br>is_draw(): Determines if the game is a draw.
<br>is_game_over(): Checks if the game has ended (either by a win or a draw).
<br>make_move(position, player): Makes a move for the specified player if the position is valid.
<br>get_available_moves(): Returns a list of available moves.

<br>Minimax Algorithm
<br>minimax(board, depth, is_maximizing): Recursively evaluates all possible moves to determine the best score for the AI or the human player.
<br>find_best_move(board): Uses the Minimax algorithm to find the optimal move for the AI.

<br>Alpha-Beta Pruning
<br>minimax_with_alpha_beta(board, depth, alpha, beta, is_maximizing): An optimized version of the Minimax algorithm that uses Alpha-Beta Pruning to reduce the number of nodes evaluated in the search tree.
<br>find_best_move_with_alpha_beta(board): Determines the best move for the AI using the Alpha-Beta Pruning version of Minimax.

<br>Game Loop
<br>play_game(): Manages the game loop, alternating turns between the human player and the AI, and displays the game outcome.

<br>Example of game session:
<br>  |   |  
---------
  |   |  
---------
  |   |  
Enter your move (0-8): 0

X |   |  
---------
  |   |  
---------
  |   |  
AI is making a move...
AI chose position 4

X |   |  
---------
  | O |  
---------
  |   |  
...
