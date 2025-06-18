
def print_board(moves, piece):
    board = [['.' for _ in range(7)] for _ in range(7)]
    center = 3
    for dx, dy in moves:
        x, y = center + dx, center + dy
        if 0 <= x < 7 and 0 <= y < 7:
            board[y][x] = 'X'
    board[center][center] = piece
    for row in board:
        print(' '.join(row))
    print()

def pawn_moves():
    return [(0, -1), (-1, -1), (1, -1)]  # forward and diagonal captures

def bishop_moves():
    return [(i, i) for i in range(-3, 4) if i != 0] + \
           [(i, -i) for i in range(-3, 4) if i != 0]

def rook_moves():
    moves = []
    for i in range(-3, 4):
        if i != 0:
            moves.append((0, i))
            moves.append((i, 0))
    return moves

def queen_moves():
    return bishop_moves() + rook_moves()

def king_moves():
    return [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]

def main():
    print("Pawn (P):")
    print_board(pawn_moves(), 'P')
    
    print("Bishop (B):")
    print_board(bishop_moves(), 'B')
    
    print("Rook (R):")
    print_board(rook_moves(), 'R')
    
    print("Queen (Q):")
    print_board(queen_moves(), 'Q')

    print("King (K):")
    print_board(king_moves(), 'K')

if __name__ == "__main__":
    main()