def is_in_check(*rows):
    try:
        board = [list(row) for row in rows]
        size = len(board)

        # Validate square board
        if any(len(row) != size for row in board):
            print("Invalid board: Not a square")
            return

        # Find King's position
        king_found = False
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'K':
                    king_x, king_y = i, j
                    king_found = True
                    break
            if king_found:
                break

        if not king_found:
            print("Invalid board: King not found")
            return

        def in_bounds(x, y):
            return 0 <= x < size and 0 <= y < size

        # Check for Rooks and Queens (horizontal + vertical)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            x, y = king_x + dx, king_y + dy
            while in_bounds(x, y):
                if board[x][y] != '.':
                    if board[x][y] in 'RQ':
                        print("Success")
                        return
                    break
                x += dx
                y += dy

        # Check for Bishops and Queens (diagonals)
        diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in diagonals:
            x, y = king_x + dx, king_y + dy
            while in_bounds(x, y):
                if board[x][y] != '.':
                    if board[x][y] in 'BQ':
                        print("Success")
                        return
                    break
                x += dx
                y += dy

        # Check for Knights
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                        (1, -2), (1, 2), (2, -1), (2, 1)]
        for dx, dy in knight_moves:
            x, y = king_x + dx, king_y + dy
            if in_bounds(x, y) and board[x][y] == 'N':
                print("Success")
                return

        # Check for Pawns (assuming they attack downward)
        for dx, dy in [(1, -1), (1, 1)]:
            x, y = king_x + dx, king_y + dy
            if in_bounds(x, y) and board[x][y] == 'P':
                print("Success")
                return

        print("Fail")

    except Exception as e:
        print("Error:", e)