import findMove as fm
matrix = [
    ["Y", "Y", "R", "R", "B", "P", "R", "OH", "G"],
    ["Y", "G", "B", "B", "P", "O", "O", "B", "B"],
    ["R", "P", "O", "Y", "R", "G", "O", "G", "R"],
    ["R", "R", "B", "Y", "B", "P", "P", "R", "G"],
    ["G", "Y", "R", "P", "Y", "B", "Y", "P", "P"],
    ["B", "R", "G", "P", "O", "P", "Y", "R", "G"],
    ["P", "G", "R", "O", "Y", "O", "C", "Y", "O"],
    ["P", "B", "G", "R", "B", "R", "O", "G", "R"],
    ["R", "R", "P", "Y", "B", "Y", "G", "P", "Y"]
]

moves = fm.countMoves(matrix, 3.5, 4, 3, 2.5)
for move in moves:
    print(move)
print("\n", fm.selectMove(moves))
# No está revisando el dulce actual