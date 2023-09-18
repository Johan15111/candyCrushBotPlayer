# FUnctions that counts how many candies will be connected
def countDown(candyMatrix, coords, candy):
    matrixHeight = len(candyMatrix)
    result = 0
    posX = coords[0]
    posY = coords[1]

    gap = 1

    while posY + gap < matrixHeight:
        if candyMatrix[posY + gap][posX] == candy:
            result += 1
        else:
            break
        gap += 1

    return result

def countUp(candyMatrix, coords, candy):
    result = 0
    posX = coords[0]
    posY = coords[1]

    gap = 1

    while posY - gap >= 0:
        if candyMatrix[posY - gap][posX] == candy:
            result += 1
        else:
            break
        gap += 1

    return result

def countLeft(candyMatrix, coords, candy):
    result = 0
    posX = coords[0]
    posY = coords[1]

    gap = 1

    while posX - gap >= 0:
        if candyMatrix[posY][posX - gap] == candy:
            result += 1
        else:
            break
        gap += 1

    return result

def countRight(candyMatrix, coords, candy):
    matrixWidth = len(candyMatrix[0])
    result = 0
    posX = coords[0]
    posY = coords[1]

    gap = 1

    while posX + gap < matrixWidth:
        if candyMatrix[posY][posX + gap] == candy:
            result += 1
        else:
            break
        gap += 1

    return result

# FUnctions that counts how many candies will be connected
# if the candy moves in any direction
def lookDown(candyMatrix, coords):
    candy = candyMatrix[coords[1]][coords[0]]
    pointCoords = [coords[0], coords[1] + 1]
    result = 1
    # Counting the horizontal line
    horizontal = (
        countLeft(candyMatrix, pointCoords, candy) +
        countRight(candyMatrix, pointCoords, candy)
        )
    if horizontal >= 2:
        result += horizontal

    # Counting the verticcal line
    vertical = countDown(candyMatrix, pointCoords, candy)
    if vertical >= 2:
        result += vertical

    return result

def lookUp(candyMatrix, coords):
    candy = candyMatrix[coords[1]][coords[0]]
    pointCoords = [coords[0], coords[1] - 1]
    result = 1
    # Counting the horizontal line
    horizontal = (
        countLeft(candyMatrix, pointCoords, candy) +
        countRight(candyMatrix, pointCoords, candy)
        )
    if horizontal >= 2:
        result += horizontal
    
    # Counting the verticcal line
    vertical = countUp(candyMatrix, pointCoords, candy)
    if vertical >= 2:
        result += vertical
    
    return result

def lookLeft(candyMatrix, coords):
    candy = candyMatrix[coords[1]][coords[0]]
    pointCoords = [coords[0] - 1, coords[1]]
    result = 1
    # Counting the horizontal line
    horizontal = countLeft(candyMatrix, pointCoords, candy)
    if horizontal >= 2:
        result += horizontal
    
    # Counting the verticcal line
    horizontal = (
        countDown(candyMatrix, pointCoords, candy) +
        countUp(candyMatrix, pointCoords, candy)
        )
    if horizontal >= 2:
        result += horizontal

    return result

def lookRight(candyMatrix, coords):
    candy = candyMatrix[coords[1]][coords[0]]
    pointCoords = [coords[0] + 1, coords[1]]
    result = 1
    # Counting the horizontal line
    horizontal = countRight(candyMatrix, pointCoords, candy)
    if horizontal >= 2:
        result += horizontal
    
    # Counting the verticcal line
    horizontal = (
        countDown(candyMatrix, pointCoords, candy) +
        countUp(candyMatrix, pointCoords, candy)
        )
    if horizontal >= 2:
        result += horizontal
        
    return result

def countMoves(candyMatrix):
    matrixHeight = len(candyMatrix)
    matrixWidth = len(candyMatrix[0])
    yRoute = range(matrixHeight - 1, -1, -1)
    xRoute = range(matrixWidth - 1)

    moves = []    
    for i in yRoute:
        for j in xRoute:
            down = 0
            up = 0
            left = 0
            right = 0
            if i != matrixHeight - 1:
                down = lookDown(candyMatrix, [j, i])
            if i != 0:
                up = lookUp(candyMatrix, [j, i])
            if j != 0:
                left = lookLeft(candyMatrix, [j, i])
            if j != matrixWidth - 1:
                right = lookRight(candyMatrix, [j, i])
            if down > 1:
                moves.append([[j, i], ["d", down]])
            if up > 1:
                moves.append([[j, i], ["u", up]])
            if left > 1:
                moves.append([[j, i], ["l", left]])
            if right > 1:
                moves.append([[j, i], ["r", right]])
    return moves

def selectMove(moves):
    best = moves[0]
    for i in moves:
        if i[1][1] > best[1][1]:
            best = i
    return [best[0], best[1][0]]