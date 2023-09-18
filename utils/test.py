import findMove as fm
matrix = [
    ["y", "y", "r", "r", "b", "p", "r", "o", "g"],
    ["y", "g", "b", "b", "p", "o", "o", "b", "o"],
    ["r", "p", "o", "y", "r", "g", "o", "g", "r"],
    ["r", "r", "b", "y", "b", "p", "p", "r", "g"],
    ["g", "y", "r", "p", "y", "b", "y", "p", "p"],
    ["b", "r", "g", "p", "o", "p", "y", "r", "g"],
    ["p", "g", "r", "o", "y", "o", "o", "y", "o"],
    ["p", "b", "g", "r", "b", "r", "o", "g", "r"],
    ["r", "r", "p", "y", "b", "y", "g", "p", "y"]
]

moves = fm.countMoves(matrix)
print(moves)
print("\n", fm.selectMove(moves))