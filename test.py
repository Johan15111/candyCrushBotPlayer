import findMove as fm
matrix = [
    ["G", "B", "P", "3", "4", "P", "G", "O", "P"],
    ["B", "Y", "O", "O", "B", "Y", "G", "B", "P"],
    ["B", "O", "B", "B", "R", "P", "B", "O", "G"],
    ["Y", "Y", "O", "G", "P", "Y", "G", "R", "R"],
    ["P", "O", "B", "Y", "GH", "O", "P", "G", "B"],
    ["G", "R", "Y", "P", "B", "B", "R", "Y", "P"],
    ["P", "BV", "B", "O", "RH", "Y", "G", "Y", "B"],
    ["G", "Y", "R", "GE", "B", "R", "YV", "P", "O"],
    ["P", "G", "O", "Y", "P", "O", "O", "G", "B"]
]

print(fm.countCandiesPerColor(matrix))
print(fm.countMoves(matrix, 3.5, 3, 3.5, 3.5))
# No está revisando el dulce actual