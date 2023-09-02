import cv2
import numpy as np
import os
import mss
import time
import concurrent.futures

class Agent:
    # Inicializar capturador de pantalla
    sct = mss.mss()

    # Dimensiones de la pantalla de juego
    monitor = {"top": 197, "left": 641, "width": 639, "height": 567}

    # Dimensiones fijas de cada cuadrícula
    tileWidth = monitor["width"] // 9
    tileHeight = monitor["height"] // 9

    candyImages = []
    referenceDict = {}

    def __init__(self):
        # Cargar imagenes de referencia
        self.candyImages, self.referenceDict = self.loadReferenceImages()

    def sensor(self):
        self.takeScreenshot()

        board = cv2.imread("screenshot.png")

        gameBoard = self.detectCandies(board, self.candyImages, self.referenceDict)

        return gameBoard

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
    
    def takeScreenshot(self):
        time.sleep(3)

        # Tomar screenshot
        sctImg = self.sct.grab(self.monitor)

        # Convertir a numpy array
        imgNp = np.array(sctImg)
        cv2.imwrite("screenshot.png", imgNp)

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
    agent = Agent()
    gameBoard = agent.sensor()

    for row in gameBoard:
        print("--".join(str(cell) if cell is not None else ' ' for cell in row))
        print()