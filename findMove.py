# FUnctions that counts how many candies will be connected
def countDown(candyMatrix, coords, candy):
    matrixHeight = len(candyMatrix)
    result = 0
    explosive = 0
    vertical = 0
    horizontal = 0
    posX = coords[0]
    posY = coords[1]

    gap = 1
    if len(candy) == 2:
        if candy[1] == "E":
            explosive += 1
        if candy[1] == "V":
            vertical += 1
        if candy[1] == "H":
            horizontal += 1

    while posY + gap < matrixHeight:
        if candyMatrix[posY + gap][posX][0] == candy[0]:
            if len(candyMatrix[posY + gap][posX]) == 2:
                if candyMatrix[posY + gap][posX][1] == "E":
                    explosive += 1
                if candyMatrix[posY + gap][posX][1] == "V":
                    vertical += 1
                if candyMatrix[posY + gap][posX][1] == "H":
                    horizontal += 1
            result += 1
        else:
            break
        gap += 1

    return [result, explosive, vertical, horizontal]

def countUp(candyMatrix, coords, candy):
    result = 0
    explosive = 0
    vertical = 0
    horizontal = 0
    posX = coords[0]
    posY = coords[1]

    gap = 1
    if len(candy) == 2:
        if candy[1] == "E":
            explosive += 1
        if candy[1] == "V":
            vertical += 1
        if candy[1] == "H":
            horizontal += 1

    while posY - gap >= 0:
        if candyMatrix[posY - gap][posX][0] == candy[0]:
            if len(candyMatrix[posY - gap][posX]) == 2:
                if candyMatrix[posY - gap][posX][1] == "E":
                    explosive += 1
                if candyMatrix[posY - gap][posX][1] == "V":
                    vertical += 1
                if candyMatrix[posY - gap][posX][1] == "H":
                    horizontal += 1
            result += 1
        else:
            break
        gap += 1

    return [result, explosive, vertical, horizontal]

def countLeft(candyMatrix, coords, candy):
    result = 0
    explosive = 0
    vertical = 0
    horizontal = 0
    posX = coords[0]
    posY = coords[1]

    gap = 1
    if len(candy) == 2:
        if candy[1] == "E":
            explosive += 1
        if candy[1] == "V":
            vertical += 1
        if candy[1] == "H":
            horizontal += 1

    while posX - gap >= 0:
        if candyMatrix[posY][posX - gap][0] == candy[0]:
            if len(candyMatrix[posY][posX - gap]) == 2:
                if candyMatrix[posY][posX - gap][1] == "E":
                    explosive += 1
                if candyMatrix[posY][posX - gap][1] == "V":
                    vertical += 1
                if candyMatrix[posY][posX - gap][1] == "H":
                    horizontal += 1
            result += 1
        else:
            break
        gap += 1

    return [result, explosive, vertical, horizontal]

def countRight(candyMatrix, coords, candy):
    matrixWidth = len(candyMatrix[0])
    result = 0
    explosive = 0
    vertical = 0
    horizontal = 0
    posX = coords[0]
    posY = coords[1]

    gap = 1
    if len(candy) == 2:
        if candy[1] == "E":
            explosive += 1
        if candy[1] == "V":
            vertical += 1
        if candy[1] == "H":
            horizontal += 1
    while posX + gap < matrixWidth:
        if candyMatrix[posY][posX + gap][0] == candy[0]:
            if len(candyMatrix[posY][posX + gap]) == 2:
                if candyMatrix[posY][posX + gap][1] == "E":
                    explosive += 1
                if candyMatrix[posY][posX + gap][1] == "V":
                    vertical += 1
                if candyMatrix[posY][posX + gap][1] == "H":
                    horizontal += 1
            result += 1
        else:
            break
        gap += 1

    return [result, explosive, vertical, horizontal]

# FUnctions that counts how many candies will be connected
# if the candy moves in any direction
def lookDown(candyMatrix, coords):
    candy = candyMatrix[coords[1]][coords[0]]
    pointCoords = [coords[0], coords[1] + 1]
    result = 1
    explosiveCandies = 0
    verticalCandies = 0
    horizontalCandies = 0
    # Counting the horizontal line
    leftCandies = countLeft(candyMatrix, pointCoords, candy)
    rightCandies = countRight(candyMatrix, pointCoords, candy)
    horizontal = leftCandies[0] + rightCandies[0]
    if horizontal >= 2:
        explosiveCandies += leftCandies[1] + rightCandies[1]
        verticalCandies += leftCandies[2] + rightCandies[2]
        horizontalCandies += leftCandies[3] + rightCandies[3]
        result += horizontal

    # Counting the verticcal line
    vertical = countDown(candyMatrix, pointCoords, candy)
    if vertical[0] >= 2:
        explosiveCandies += vertical[1]
        verticalCandies += vertical[2]
        horizontalCandies += vertical[3]
        result += vertical[0]

    return [result, explosiveCandies, verticalCandies, horizontalCandies]

def lookUp(candyMatrix, coords):
    candy = candyMatrix[coords[1]][coords[0]]
    pointCoords = [coords[0], coords[1] - 1]
    result = 1
    explosiveCandies = 0
    verticalCandies = 0
    horizontalCandies = 0
    # Counting the horizontal line
    leftCandies = countLeft(candyMatrix, pointCoords, candy)
    rightCandies = countRight(candyMatrix, pointCoords, candy)
    horizontal = leftCandies[0] + rightCandies[0]

    if horizontal >= 2:
        explosiveCandies += leftCandies[1] + rightCandies[1]
        verticalCandies += leftCandies[2] + rightCandies[2]
        horizontalCandies += leftCandies[3] + rightCandies[3]
        result += horizontal
    
    # Counting the verticcal line
    vertical = countUp(candyMatrix, pointCoords, candy)
    if vertical[0] >= 2:
        explosiveCandies += vertical[1]
        verticalCandies += vertical[2]
        horizontalCandies += vertical[3]
        result += vertical[0]
    
    return [result, explosiveCandies, verticalCandies, horizontalCandies]

def lookLeft(candyMatrix, coords):
    candy = candyMatrix[coords[1]][coords[0]]
    pointCoords = [coords[0] - 1, coords[1]]
    result = 1
    explosiveCandies = 0
    verticalCandies = 0
    horizontalCandies = 0
    # Counting the horizontal line
    horizontal = countLeft(candyMatrix, pointCoords, candy)
    if horizontal[0] >= 2:
        explosiveCandies += horizontal[1]
        verticalCandies += horizontal[2]
        horizontalCandies += horizontal[3]
        result += horizontal[0]
    
    # Counting the verticcal line
    downCandies = countDown(candyMatrix, pointCoords, candy)
    upCandies = countUp(candyMatrix, pointCoords, candy)
    vertical = downCandies[0] + upCandies[0]

    if vertical >= 2:
        explosiveCandies += downCandies[1] + upCandies[1]
        verticalCandies += downCandies[2] + upCandies[1]
        horizontalCandies += downCandies[3] + upCandies[1]
        result += vertical

    return [result, explosiveCandies, verticalCandies, horizontalCandies]

def lookRight(candyMatrix, coords):
    candy = candyMatrix[coords[1]][coords[0]]
    pointCoords = [coords[0] + 1, coords[1]]
    result = 1
    explosiveCandies = 0
    verticalCandies = 0
    horizontalCandies = 0
    # Counting the horizontal line
    horizontal = countRight(candyMatrix, pointCoords, candy)
    if horizontal[0] >= 2:
        explosiveCandies += horizontal[1]
        verticalCandies += horizontal[2]
        horizontalCandies += horizontal[3]
        result += horizontal[0]
    
    # Counting the verticcal line
    downCandies = countDown(candyMatrix, pointCoords, candy)
    upCandies = countUp(candyMatrix, pointCoords, candy)
    vertical = downCandies[0] + upCandies[0]

    if vertical >= 2:
        explosiveCandies += downCandies[1] + upCandies[1]
        verticalCandies += downCandies[2] + upCandies[1]
        horizontalCandies += downCandies[3] + upCandies[1]       
        result += vertical

    return [result, explosiveCandies, verticalCandies, horizontalCandies]

def countCandiesPerColor(candyMatrix):
    candiesPerColor = {}
    for row in candyMatrix:
        for candy in row:
            foundedFlag = False
            for founded in candiesPerColor:
                if candy[0] == founded:
                    candiesPerColor[founded] += 1
                    foundedFlag = True
            if foundedFlag != True:
                candiesPerColor[candy[0]] = 1
    return candiesPerColor

# FUnction that find the posible moves in the matrix and assign a score
def countMoves(candyMatrix, brownScore, explosiveMultiplier, verticalMultiplier, 
               horizontalMultiplier):
    matrixHeight = len(candyMatrix)
    matrixWidth = len(candyMatrix[0])
    yRoute = range(matrixHeight - 1, -1, -1)
    xRoute = range(matrixWidth - 1)

    moves = []    
    for i in yRoute:
        for j in xRoute:
            down = 0
            downExplosive = 0
            downVertical = 0
            downHorizontal = 0

             # Verify if can be joint a brown candy with a super candy
            if candyMatrix[i][j][0] == "C":
                if i != matrixHeight - 1:
                    if candyMatrix[i + 1][j][0] == "C":
                        return ([i, j], "d")
                if i != 0:
                    if candyMatrix[i - 1][j][0] == "C":
                        return ([i, j], "u")
                if j != 0:
                    if candyMatrix[i][j - 1] == "C":
                        return ([i, j], "l")
                if j != matrixWidth - 1:
                    if candyMatrix[i][j + 1][0] == "C":
                        return ([i, j], "r")
                    
            # Verify if can be joint a brown candy with a super candy
            if candyMatrix[i][j][0] == "C":
                if i != matrixHeight - 1:
                    if len(candyMatrix[i + 1][j]) == 2:
                        return ([i, j], "d")
                if i != 0:
                    if len(candyMatrix[i - 1][j]) == 2:
                        return ([i, j], "u")
                if j != 0:
                    if len(candyMatrix[i][j - 1]) == 2:
                        return ([i, j], "l")
                if j != matrixWidth - 1:
                    if len(candyMatrix[i][j + 1]) == 2:
                        return ([i, j], "r")
                    
            # Verify if found 2 super candies joint
            if len(candyMatrix[i][j]) == 2:
                if i != matrixHeight - 1:
                    if len(candyMatrix[i + 1][j]) == 2:
                        return ([i, j], "d")
                if i != 0:
                    if len(candyMatrix[i - 1][j]) == 2:
                        return ([i, j], "u")
                if j != 0:
                    if len(candyMatrix[i][j - 1]) == 2:
                        return ([i, j], "l")
                if j != matrixWidth - 1:
                    if len(candyMatrix[i][j + 1]) == 2:
                        return ([i, j], "r")

            if i != matrixHeight - 1:
                downCandies = lookDown(candyMatrix, [j, i])
                down = downCandies[0]
                downExplosive = downCandies[1]
                downVertical = downCandies[2]
                downHorizontal = downCandies[3]

            up = 0
            upExplosive = 0
            upVertical = 0
            upHorizontal = 0
            if i != 0:
                upCandies = lookUp(candyMatrix, [j, i])
                up = upCandies[0]
                upExplosive = upCandies[1]
                upVertical = upCandies[2]
                upHorizontal = upCandies[3]

            left = 0
            leftExplosive = 0
            leftVertical = 0
            leftHorizontal = 0
            if j != 0:
                leftCandies = lookLeft(candyMatrix, [j, i])
                left = leftCandies[0]
                leftExplosive = leftCandies[1]
                leftVertical = leftCandies[2]
                leftHorizontal = leftCandies[3]

            right = 0
            rightExplosive = 0
            rightVertical = 0
            rightHorizontal = 0
            if j != matrixWidth - 1:
                rightCandies = lookRight(candyMatrix, [j, i])
                right = rightCandies[0]
                rightExplosive = rightCandies[1]
                rightVertical = rightCandies[2]
                rightHorizontal = rightCandies[3]
            
            # Find simple combos
            if down >= 3:
                downScore = (
                    down + 
                    downExplosive * explosiveMultiplier +
                    downVertical * verticalMultiplier +
                    downHorizontal * horizontalMultiplier
                )
                moves.append([[j, i], ["d", downScore]])

            if up >= 3:
                upScore = (
                    up + 
                    upExplosive * explosiveMultiplier +
                    upVertical * verticalMultiplier +
                    upHorizontal * horizontalMultiplier
                )
                moves.append([[j, i], ["u", upScore]])

            if left >= 3:
                leftScore = (
                    left + 
                    leftExplosive * explosiveMultiplier +
                    leftVertical * verticalMultiplier +
                    leftHorizontal * horizontalMultiplier
                )
                moves.append([[j, i], ["l", leftScore]])

            if right >= 3:
                rightScore = (
                    right + 
                    rightExplosive * explosiveMultiplier +
                    rightVertical * verticalMultiplier +
                    rightHorizontal * horizontalMultiplier
                )
                moves.append([[j, i], ["r", rightScore]])

            # Rate brown candies
            if candyMatrix[i][j][0] == "C":
                candiesPerColor = countCandiesPerColor(candyMatrix)
                bDown = 0
                bUp = 0
                bLeft = 0
                bRight = 0
                if i != matrixHeight - 1:
                    bDown = candiesPerColor[candyMatrix[i + 1][j][0]]
                if i != 0:
                    bUp = candiesPerColor[candyMatrix[i - 1][j][0]]
                if j != 0:
                    bLeft = candiesPerColor[candyMatrix[i][j - 1][0]]
                if j != matrixWidth - 1:
                    bRight = candiesPerColor[candyMatrix[i][j + 1][0]]
                highest = max(bDown, bUp, bLeft, bRight)

                if highest == bDown:
                    moves.append([[j, i], ["d", brownScore]])
                elif highest == bUp:
                    moves.append([[j, i], ["u", brownScore]])
                elif highest == bLeft:
                    moves.append([[j, i], ["l", brownScore]])
                else:
                    moves.append([[j, i], ["r", brownScore]])

    if len(moves) == 0:
        return ([0, 0], "d")
    best = moves[0]
    for i in moves:
        if i[1][1] > best[1][1]:
            best = i
    return ([best[0][1], best[0][0]], best[1][0])
    