def solve_n_queens(n):
    def backtrack(row, cols, diag1, diag2, board, res):
        if row == n:
            res.append([''.join(r) for r in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = 'Q'
            backtrack(row + 1, cols, diag1, diag2, board, res)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            board[row][col] = '.'
    res = []
    board = [['.'] * n for _ in range(n)]
    backtrack(0, set(), set(), set(), board, res)
    return res

# Output
solutions = solve_n_queens(4)
for solution in solutions[:2]:
    print(solution)
# Sample: ['.Q..', '...Q', 'Q...', '..Q.']
