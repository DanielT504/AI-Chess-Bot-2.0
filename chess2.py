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
    
def evaluate_board(board, turn):
    #print("{}".format(turn))
    '''
    if turn == chess.BLACK:
        print("black")
    else:
        print("white")
    '''
    
    piece_weights = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
    }

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

    total_evaluation = 0
    pawns = {}
    isolated_pawns = {}
    doubled_pawns = {}
    blocked_pawns = {}
    black_pawns = {}
    black_isolated_pawns = {}
    black_doubled_pawns = {}
    black_blocked_pawns = {}
    
    for rank in range(8):
        for file in range(8):
            square = chess.square(file, rank)
            piece = board.piece_at(square)
            if piece is not None:
                if piece.piece_type == chess.PAWN:
                    if piece.color == chess.WHITE:
                        pawn_value = chess.PAWN + p_w[rank][file]
                    else:
                        pawn_value = -chess.PAWN - p_b[rank][file]
                    
                    total_evaluation += pawn_value
                    if piece.color == chess.WHITE:
                        if file in pawns:
                            pawns[file].append(pawn_value)
                        else:
                            pawns[file] = [pawn_value]
                            
                        if file - 1 not in pawns and file + 1 not in pawns:
                            isolated_pawns[file] = True
                            
                        if file in doubled_pawns:
                            doubled_pawns[file] += 1
                        else:
                            doubled_pawns[file] = 1
                            
                        if piece.color == chess.WHITE:
                            blocking_rank = rank - 1
                        else:
                            blocking_rank = rank + 1
                        if blocking_rank >= 0 and blocking_rank <= 7:
                            blocking_square = chess.square(file, blocking_rank)
                            blocking_piece = board.piece_at(blocking_square)
                            if blocking_piece is not None and blocking_piece.piece_type == chess.PAWN:
                                blocked_pawns[file] = True
                    else:
                        if file in black_pawns:
                            black_pawns[file].append(pawn_value)
                        else:
                            black_pawns[file] = [pawn_value]
                        
                        if file - 1 not in black_pawns and file + 1 not in black_pawns:
                            black_isolated_pawns[file] = True
                        
                        if file in black_doubled_pawns:
                            black_doubled_pawns[file] += 1
                        else:
                            black_doubled_pawns[file] = 1
                        
                        blocking_rank = rank + 1
                        if blocking_rank >= 0 and blocking_rank <= 7:
                            blocking_square = chess.square(file, blocking_rank)
                            blocking_piece = board.piece_at(blocking_square)
                            if blocking_piece is not None and blocking_piece.piece_type == chess.PAWN:
                                black_blocked_pawns[file] = True
                        
                elif piece.piece_type == chess.ROOK:
                    total_evaluation += chess.ROOK * (1 if piece.color == chess.WHITE else -1) + (r_w[rank][file] if piece.color == chess.WHITE else -r_b[rank][file])
                elif piece.piece_type == chess.KNIGHT:
                    total_evaluation += chess.KNIGHT * (1 if piece.color == chess.WHITE else -1) + (n_w[rank][file] if piece.color == chess.WHITE else -n_b[rank][file])
                elif piece.piece_type == chess.BISHOP:
                    total_evaluation += chess.BISHOP * (1 if piece.color == chess.WHITE else -1) + (b_w[rank][file] if piece.color == chess.WHITE else -b_b[rank][file])
                elif piece.piece_type == chess.QUEEN:
                    total_evaluation += chess.QUEEN * (1 if piece.color == chess.WHITE else -1) + (q_w[rank][file] if piece.color == chess.WHITE else -q_b[rank][file])
                elif piece.piece_type == chess.KING:
                    total_evaluation += chess.KING * (1 if piece.color == chess.WHITE else -1) + (k_w[rank][file] if piece.color == chess.WHITE else -k_b[rank][file])
    
    total_evaluation += len(isolated_pawns) * (-100)
    total_evaluation += len(doubled_pawns) * (-200)
    total_evaluation += len(blocked_pawns) * (-100)
    total_evaluation += len(black_isolated_pawns) * (100)
    total_evaluation += len(black_doubled_pawns) * (200)
    total_evaluation += len(black_blocked_pawns) * (100)
    
    player_legal_moves = list(board.legal_moves)
    #print("player_legal_moves: {}".format(player_legal_moves))
    board.turn = not board.turn  # Switch to opponent's turn
    ai_legal_moves = list(board.legal_moves)
    #print("ai_legal_moves: {}".format(ai_legal_moves))
    board.turn = not board.turn  # Switch to opponent's turn
    mobility_score = 10 * (len(ai_legal_moves) - len(player_legal_moves))
    total_evaluation += mobility_score
    
    captures_score = 5 * len([move for move in ai_legal_moves if board.is_capture(move)])
    total_evaluation += captures_score
    captured_score = -5 * len([move for move in player_legal_moves if board.is_capture(move)])
    total_evaluation += captured_score
    
    threatened_pieces_score = 0.0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.color == chess.BLACK:
            if any(move.to_square == square and board.is_capture(move) for move in player_legal_moves):
                threatened_pieces_score -= 10 * piece_weights.get(piece.piece_type, 0)
    total_evaluation += threatened_pieces_score
    
    threatening_pieces_score = 0.0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.color == chess.WHITE:
            if any(move.to_square == square and board.is_capture(move) for move in ai_legal_moves):
                #weights commented until balanced
                if piece.piece_type != chess.KING or not board.is_check():
                    threatened_pieces_score = threatened_pieces_score
                    #threatening_pieces_score += piece_weights.get(piece.piece_type, 0)
                else:
                    threatening_piece_square = get_threatening_piece_square(board, square)
                    if board.is_checkmate():
                        threatening_pieces_score = float('inf')
                    elif is_square_safe(board, threatening_piece_square):
                        threatened_pieces_score = threatened_pieces_score
                        #threatening_pieces_score += piece_weights.get(piece.piece_type, 0)
    total_evaluation += threatening_pieces_score
    
    '''
    print("Total Evaluation: {}".format(total_evaluation))
    print("Isolated Pawns: {}".format(isolated_pawns))
    print("Doubled Pawns: {}".format(doubled_pawns))
    print("Blocked Pawns: {}".format(blocked_pawns))
    print("Black Pawns: {}".format(black_pawns))
    print("Black Isolated Pawns: {}".format(black_isolated_pawns))
    print("Black Doubled Pawns: {}".format(black_doubled_pawns))
    print("Black Blocked Pawns: {}".format(black_blocked_pawns))
    #print("Player Legal Moves: {}".format(player_legal_moves))
    #print("Opponent Legal Moves: {}".format(opponent_legal_moves))
    print("Mobility Score: {}".format(mobility_score))
    print("Captures Score: {}".format(captured_score))
    print("Captures Score: {}".format(captures_score))
    print("Threatened Pieces Score: {}".format(threatened_pieces_score))
    print("Threatening Pieces Score: {}\n".format(threatening_pieces_score))
    '''
    
    if turn == chess.BLACK:
        total_evaluation = -total_evaluation
    
    return total_evaluation

def get_threatening_piece_square(board, target_square):
    piece = board.piece_at(target_square)
    if piece is not None:
        attackers = board.attackers(not piece.color, target_square)
        if attackers:
            return attackers.pop()
    return None

def is_square_safe(board, square):
    piece = board.piece_at(square)
    if piece is not None:
        attackers = board.attackers(not piece.color, square)
        return len(attackers) == 0
    return True

def alphabeta(board, depth, alpha, beta, maximizing_player):
    best_value = float('-inf') if maximizing_player else float('inf')
    if depth:
        if maximizing_player:
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
            print(" " * (depth) + f"Depth {depth} Max: {best_value}")
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
            print(" " * (depth) + f"Depth {depth} Min: {best_value}")
            return best_value
    else:
        x=evaluate_board(board, not maximizing_player)
        print(" " * (depth) + f"Depth {depth} Score: {x}")
        return x


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
    depth = 2  # 5 takes ~3min for the first move, 4 takes ~1min, 3 takes ~3sec
    legal_moves = list(board.legal_moves)

    if len(legal_moves) == 0:
        print("Game Over - No valid moves available")
        return

    best_move = None
    best_score = -float('inf')

    for move in legal_moves:
        board.push(move)
        score = alphabeta(board, depth - 1, -float('inf'), float('inf'), False)
        print("move: {}".format(move))
        board.pop()
        print("score: {}\n".format(score))
        if score > best_score:
            best_score = score
            best_move = move
    print("best: {}".format(best_score))
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
