import findMove as fm
matrix = [
    ["Y", "R", "G", "3", "4", "P", "B", "R", "G"],
    ["B", "R", "G", "P", "R", "P", "G", "G", "P"],
    ["B", "P", "YV", "O", "B", "Y", "Y", "P", "P"],
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