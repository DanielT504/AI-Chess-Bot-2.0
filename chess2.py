import chess
import tkinter as tk
from tkinter import messagebox

# Global variables for GUI
board_buttons = {}
selected_square = None
last_move_start = None
last_move_end = None

# Board dimensions
BOARD_WIDTH = BOARD_HEIGHT = 600
SQUARE_SIZE = BOARD_WIDTH // 8
MAX_DEPTH = 3

# Colors
LIGHT_SQUARE_COLOR = "#F0D9B5"  # Hexadecimal value for (240, 217, 181)
DARK_SQUARE_COLOR = "#B58863"  # Hexadecimal value for (181, 136, 99)
SELECTED_SQUARE_COLOR = "#7A9ECA"  # Hexadecimal value for (122, 158, 202)
LAST_MOVE_COLOR = "#F9E79F"  # Hexadecimal value for red

# Initialize the chess board
board = chess.Board()

#using piece square tables from the simplified evaluation fucntion
p_w = [
[ 0,  0,  0,  0,  0,  0,  0,  0],
[50, 50, 50, 50, 50, 50, 50, 50],
[10, 10, 20, 30, 30, 20, 10, 10],
[ 5,  5, 10, 25, 25, 10,  5,  5],
[ 0,  0,  0, 20, 20,  0,  0,  0],
[ 5, -5,-10,  0,  0,-10, -5,  5],
[ 5, 10, 10,-20,-20, 10, 10,  5],
[ 0,  0,  0,  0,  0,  0,  0,  0]
]

p_b = [
[ 0,  0,  0,  0,  0,  0,  0,  0],
[ 5, 10, 10,-20,-20, 10, 10,  5],
[ 5, -5,-10,  0,  0,-10, -5,  5],
[ 0,  0,  0, 20, 20,  0,  0,  0],
[ 5,  5, 10, 25, 25, 10,  5,  5],
[10, 10, 20, 30, 30, 20, 10, 10],
[50, 50, 50, 50, 50, 50, 50, 50],
[ 0,  0,  0,  0,  0,  0,  0,  0]
]

n_w = [
[-50, -40, -30, -30, -30, -30, -40, -50],
[-40, -20,   0,   0,   0,   0, -20, -40],
[-30,   0,  10,  15,  15,  10,   0, -30],
[-30,   5,  15,  20,  20,  15,   5, -30],
[-30,   0,  15,  20,  20,  15,   0, -30],
[-30,   5,  10,  15,  15,  10,   5, -30],
[-40, -20,   0,   5,   5,   0, -20, -40],
[-50, -40, -30, -30, -30, -30, -40, -50]
]

n_b = [
[-50, -40, -30, -30, -30, -30, -40, -50],
[-40, -20,   0,   5,   5,   0, -20, -40],
[-30,   5,  10,  15,  15,  10,   5, -30],
[-30,   0,  15,  20,  20,  15,   0, -30],
[-30,   5,  15,  20,  20,  15,   5, -30],
[-30,   0,  10,  15,  15,  10,   0, -30],
[-40, -20,   0,   0,   0,   0, -20, -40],
[-50, -40, -30, -30, -30, -30, -40, -50]
]

b_w = [
[-20, -10, -10, -10, -10, -10, -10, -20],
[-10,   0,   0,   0,   0,   0,   0, -10],
[-10,   0,   5,  10,  10,   5,   0, -10],
[-10,   5,   5,  10,  10,   5,   5, -10],
[-10,   0,  10,  10,  10,  10,   0, -10],
[-10,  10,  10,  10,  10,  10,  10, -10],
[-10,   5,   0,   0,   0,   0,   5, -10],
[-20, -10, -10, -10, -10, -10, -10, -20]
]

b_b = [
[-20, -10, -10, -10, -10, -10, -10, -20],
[-10,   5,   0,   0,   0,   0,   5, -10],
[-10,  10,  10,  10,  10,  10,  10, -10],
[-10,   0,  10,  10,  10,  10,   0, -10],
[-10,   5,   5,  10,  10,   5,   5, -10],
[-10,   0,   5,  10,  10,   5,   0, -10],
[-10,   0,   0,   0,   0,   0,   0, -10],
[-20, -10, -10, -10, -10, -10, -10, -20]
]

r_w = [
[ 0,  0,  0,  0,  0,  0,  0,  0],
[ 5, 10, 10, 10, 10, 10, 10,  5],
[-5,  0,  0,  0,  0,  0,  0, -5],
[-5,  0,  0,  0,  0,  0,  0, -5],
[-5,  0,  0,  0,  0,  0,  0, -5],
[-5,  0,  0,  0,  0,  0,  0, -5],
[-5,  0,  0,  0,  0,  0,  0, -5],
[ 0,  0,  0,  5,  5,  0,  0,  0]
]

r_b = [
[ 0,  0,  0,  5,  5,  0,  0,  0],
[-5,  0,  0,  0,  0,  0,  0, -5],
[-5,  0,  0,  0,  0,  0,  0, -5],
[-5,  0,  0,  0,  0,  0,  0, -5],
[-5,  0,  0,  0,  0,  0,  0, -5],
[-5,  0,  0,  0,  0,  0,  0, -5],
[ 5, 10, 10, 10, 10, 10, 10,  5],
[ 0,  0,  0,  0,  0,  0,  0,  0]
]

q_w = [
[-20, -10, -10,  -5,  -5, -10, -10, -20],
[-10,   0,   0,   0,   0,   0,   0, -10],
[-10,   0,   5,   5,   5,   5,   0, -10],
[ -5,   0,   5,   5,   5,   5,   0,  -5],
[  0,   0,   5,   5,   5,   5,   0,  -5],
[-10,   5,   5,   5,   5,   5,   0, -10],
[-10,   0,   5,   0,   0,   0,   0, -10],
[-20, -10, -10,  -5,  -5, -10, -10, -20]
]

q_b = [
[-20, -10, -10,  -5,  -5, -10, -10, -20],
[-10,   0,   5,   0,   0,   0,   0, -10],
[-10,   5,   5,   5,   5,   5,   0, -10],
[  0,   0,   5,   5,   5,   5,   0,  -5],
[ -5,   0,   5,   5,   5,   5,   0,  -5],
[ -5,   0,   5,   5,   5,   5,   0, -10],
[-10,   0,   0,   0,   0,   0,   0, -10],
[-20, -10, -10,  -5,  -5, -10, -10, -20]
]

#not great for end game
k_w = [
[-30, -40, -40, -50, -50, -40, -40, -30],
[-30, -40, -40, -50, -50, -40, -40, -30],
[-30, -40, -40, -50, -50, -40, -40, -30],
[-30, -40, -40, -50, -50, -40, -40, -30],
[-20, -30, -30, -40, -40, -30, -30, -20],
[-10, -20, -20, -20, -20, -20, -20, -10],
[ 20,  20,   0,   0,   0,   0,  20,  20],
[ 20,  30,  10,   0,   0,  10,  30,  20]
]

k_b = [
[ 20,  30,  10,   0,   0,  10,  30,  20],
[ 20,  20,   0,   0,   0,   0,  20,  20],
[-10, -20, -20, -20, -20, -20, -20, -10],
[-20, -30, -30, -40, -40, -30, -30, -20],
[-30, -40, -40, -50, -50, -40, -40, -30],
[-30, -40, -40, -50, -50, -40, -40, -30],
[-30, -40, -40, -50, -50, -40, -40, -30],
[-30, -40, -40, -50, -50, -40, -40, -30]
]
    
def evaluate_board(board):
    #to change
    total_evaluation = 0
    for rank in range(8):
        for file in range(8):
            square = chess.square(file, rank)
            piece = board.piece_at(square)
            if piece is not None:
                if piece.piece_type == chess.PAWN:
                    total_evaluation += 100 + (p_w[rank][file] if piece.color == chess.WHITE else p_b[rank][file])
                elif piece.piece_type == chess.ROOK:
                    total_evaluation += 500 + (r_w[rank][file] if piece.color == chess.WHITE else r_b[rank][file])
                elif piece.piece_type == chess.KNIGHT:
                    total_evaluation += 320 + (n_w[rank][file] if piece.color == chess.WHITE else n_b[rank][file])
                elif piece.piece_type == chess.BISHOP:
                    total_evaluation += 330 + (b_w[rank][file] if piece.color == chess.WHITE else b_b[rank][file])
                elif piece.piece_type == chess.QUEEN:
                    total_evaluation += 900 + (q_w[rank][file] if piece.color == chess.WHITE else q_b[rank][file])
                elif piece.piece_type == chess.KING:
                    total_evaluation += 20000 + (k_w[rank][file] if piece.color == chess.WHITE else k_b[rank][file])
    print("{}\n".format(total_evaluation))
    return total_evaluation

def alphabeta(board, depth, alpha, beta, maximizing_player):
    best_value = float('inf')
    if depth:
        if maximizing_player:
            best_value = -best_value
            for move in list(board.legal_moves):
                board.push(move)
                min_player = not maximizing_player
                recurse = alphabeta(board, depth-1, alpha, beta, min_player)
                if best_value < recurse:
                    best_value = recurse
                board.pop()
                if best_value > alpha:
                    alpha = best_value
                if alpha >= beta:
                    break
            return best_value
        else:
            for move in list(board.legal_moves):
                board.push(move)
                min_player = not maximizing_player
                recurse = alphabeta(board, depth-1, alpha, beta, min_player)
                if best_value > recurse:
                    best_value = recurse
                board.pop()
                if best_value < beta:
                    beta = best_value
                if alpha >= beta:
                    break
            return best_value        
    else:
        return evaluate_board(board)


def on_square_click(square):
    global selected_square
    if selected_square is None:
        selected_square = square
    else:
        move = chess.Move(selected_square, square)
        if move in board.legal_moves:
            board.push(move)
            if (
                board.is_checkmate()
                or board.is_stalemate()
                or board.is_insufficient_material()
                or board.is_seventyfive_moves()
                or board.is_fivefold_repetition()
            ):
                messagebox.showinfo("Game Over", "Game Over!")
            else:
                # Check if the move resulted in pawn promotion
                if move.promotion:
                    promotion_piece = move.promotion
                    # Manually set the promoted piece on the board
                    board.set_piece_at(square, chess.Piece.from_symbol(promotion_piece))
                refresh_board()
                selected_square = None
                make_ai_move()
                refresh_board()
        else:
            messagebox.showinfo("Invalid Move", "Invalid move. Please try again.")
            selected_square = None


def refresh_board():
    for square, button in board_buttons.items():
        piece = board.piece_at(square)
        piece_symbol = piece.symbol() if piece else ""
        button["text"] = piece_symbol

        button_color = LIGHT_SQUARE_COLOR if (chess.square_file(square) + chess.square_rank(square)) % 2 == 0 else DARK_SQUARE_COLOR
        if square == selected_square:
            button_color = SELECTED_SQUARE_COLOR
        elif square == last_move_start or square == last_move_end:
            button_color = LAST_MOVE_COLOR

        button["bg"] = button_color

def make_ai_move():
    global last_move_start, last_move_end
    depth = 2  # Adjust the depth according to your preference
    legal_moves = list(board.legal_moves)

    if len(legal_moves) == 0:
        print("Game Over - No valid moves available")
        return

    best_move = None
    best_score = -float('inf')

    for move in legal_moves:
        board.push(move)
        score = alphabeta(board, depth - 1, -float('inf'), float('inf'), False)
        board.pop()
        print("score: {}".format(score))
        if score > best_score:
            best_score = score
            best_move = move

    if best_move is not None:
        last_move_start = best_move.from_square
        last_move_end = best_move.to_square
        board.push(best_move)
    else:
        print("No valid move found by AI")


def create_board_ui(root):
    global board_buttons
    board_frame = tk.Frame(root)
    board_frame.pack()
    for row in range(8):
        for col in range(8):
            square = chess.square(col, 7 - row)
            button = tk.Button(board_frame, width=5, height=2, command=lambda sq=square: on_square_click(sq))
            button.grid(row=row, column=col)
            board_buttons[square] = button


def play_chess():
    root = tk.Tk()
    root.title("Chess")
    create_board_ui(root)
    refresh_board()
    root.mainloop()


# Example usage
play_chess()
