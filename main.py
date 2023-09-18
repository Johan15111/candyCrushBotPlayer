import cv2
import numpy as np
import os
import mss
import time
import concurrent.futures
import pyautogui
import easyocr
import findMove as fm

class Agent:
    # Inicializar capturador de pantalla
    sct = mss.mss()

    # Dimensiones de la pantalla de juego
    monitor = {"top": 197, "left": 641, "width": 639, "height": 567}
    scoreMonitor = {"top": 275, "left": 555, "width": 75, "height": 21}

    # Dimensiones fijas de cada cuadrícula
    tileWidth = monitor["width"] // 9
    tileHeight = monitor["height"] // 9

    candyImages = []
    referenceDict = {}

    score = 0

    def __init__(self):
        # Cargar imagenes de referencia
        self.candyImages, self.referenceDict = self.loadReferenceImages()
        self.scoreReader = easyocr.Reader(['en'], gpu=False)

    def sensor(self):
        board = self.takeScreenshot(self.monitor)

        gameBoard = self.detectCandies(board, self.candyImages, self.referenceDict)

        return gameBoard
    
    def sensorScoreOCR(self, monitor=scoreMonitor):
        currentScore = 1

        while self.score != currentScore:
            scoreImage = self.takeScreenshot(monitor)
            currentScore = self.scoreReader.readtext(scoreImage)
            try:
                currentScore = int(currentScore[0][-2])
                self.score = currentScore
            except:
                pass
            time.sleep(0.4)
        
        print("Puntaje actual: ", self.score)
    
    def takeScreenshot(self, monitor):
        # Tomar screenshot
        sctImg = self.sct.grab(monitor)

        # Convertir a numpy array
        imgNp = np.array(sctImg)

        return cv2.cvtColor(imgNp, cv2.COLOR_BGRA2BGR)
    
    def actuator(self, action):
        coordinates, direction = action

        # Convierte las coordenadas en valores enteros
        row = int(coordinates[0])
        col = int(coordinates[1])

        # Calcula las coordenadas en píxeles del centro de la cuadrícula
        x_center = self.monitor["left"] + (col + 0.5) * self.tileWidth
        y_center = self.monitor["top"] + (row + 0.5) * self.tileHeight

        pyautogui.moveTo(x_center, y_center)
        pyautogui.click()

        # Realiza el movimiento según la dirección indicada
        if direction == "u":
            pyautogui.moveRel(0, -self.tileHeight)
        elif direction == "d":
            pyautogui.moveRel(0, self.tileHeight)
        elif direction == "l":
            pyautogui.moveRel(-self.tileWidth, 0)
        elif direction == "r":
            pyautogui.moveRel(self.tileWidth, 0)

        pyautogui.click()

    def loadReferenceImages(self):
        candyImages = []
        referenceDict = {}

        # Cargar las imágenes de referencia y crear un diccionario con índices para los nombres de los archivos
        for idx, img in enumerate(os.listdir("candyImages")):
            candyImages.append(cv2.imread(os.path.join("candyImages", img)))

            # Eliminar cualquier número del nombre del archivo antes de guardarlo en el diccionario
            name = ''.join(filter(lambda x: not x.isdigit(), os.path.splitext(img)[0]))
            referenceDict[idx] = name

        return candyImages, referenceDict

    def detectCandies(self, board, candyImages, referenceDict):
        inicio = time.time()
        boardHeight, boardWidth = board.shape[:2]
        
        # Matriz 9x9 para los dulces del tablero
        gameBoard = [[None] * 9 for _ in range(9)]
        
        def process_tile(x, y, row, col):
            # Recorta la cuadrícula actual del tablero
            tile = board[y : y + self.tileHeight, x : x + self.tileWidth]

            # Variables para el cálculo de la imagen de dulce más similar
            maxVal = 0
            maxIdx = None

            for idx, candy in enumerate(candyImages):
                # Búsqueda de plantilla para encontrar la similitud entre
                # la cuadrícula y la imagen de dulce actual
                res = cv2.matchTemplate(tile, candy, cv2.TM_CCOEFF_NORMED)

                # Encuentra la ubicación y valor máximo en el resultado
                _, maxRes, _, maxLoc = cv2.minMaxLoc(res)

                # Actualiza las variables si se encuentra una coincidencia más cercana
                if maxRes > maxVal:
                    maxVal = maxRes
                    maxIdx = idx
            
            if maxIdx is not None:
                candy_name = referenceDict[maxIdx]
                gameBoard[row][col] = candy_name
        
        # Utilizar concurrent.futures para paralelizar la detección
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for y in range(0, boardHeight, self.tileHeight):
                for x in range(0, boardWidth, self.tileWidth):
                    row = y // self.tileHeight
                    col = x // self.tileWidth
                    executor.submit(process_tile, x, y, row, col)
        
        fin = time.time()
        print("Tiempo de ejecución deteccion: ", (fin - inicio) * 1000)
        
        return gameBoard

if __name__ == "__main__":
    time.sleep(3)

    agent = Agent()

    while True:
        gameBoard = agent.sensor()

        movements = fm.countMoves(gameBoard)
        bestMove = fm.selectMove(movements)
        
        agent.actuator(bestMove)
        agent.sensorScoreOCR()

    """ for row in gameBoard:
        print("--".join(str(cell) if cell is not None else ' ' for cell in row)) """