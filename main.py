import cv2
import numpy as np
import os
import mss
import time

def loadReferenceImages():
    candyImages = []
    for img in os.listdir("candyImages"):
        candyImages.append(cv2.imread(os.path.join("candyImages", img)))

    return candyImages

def takeScreenshot():
    time.sleep(3)
    sct_img = sct.grab(monitor)

    # Convertir a numpy array
    img_np = np.array(sct_img)
    cv2.imwrite("screenshot.png", img_np)

def detectCandies(board, candyImages):
    boardHeight, boardWidth = board.shape[:2]
    for y in range(0, boardHeight, tileHeight):
        for x in range(0, boardWidth, tileWidth):
        
            # Extrae la cuadrícula 
            tile = board[y:y+tileHeight, x:x+tileWidth]
            
            # Compara con cada imagen de dulce
            max_val = 0
            max_idx = None
            for idx, candy in enumerate(candyImages):
                res = cv2.matchTemplate(tile, candy, cv2.TM_CCOEFF_NORMED) 
                _, max_res, _, _ = cv2.minMaxLoc(res)
                if max_res > max_val:
                    max_val = max_res
                    max_idx = idx
            
            # max_idx tiene el índice del dulce detectado
            print(f'Dulce {max_idx} detectado en x={x}, y={y}')

if __name__ == "__main__":
    # Inicializar mss
    sct = mss.mss()

    # Dimensiones de la pantalla de juego
    monitor = {"top": 240, "left": 560, "width": 805, "height": 717}

    # Dimensiones fijas de cada cuadrícula
    tileWidth = 80
    tileHeight = 85

    # Cargar imagenes de referencia
    candyImages = loadReferenceImages()

    inicio = time.time()
    takeScreenshot()
    fin = time.time()

    # Imprime el tiempo en milisegundos
    print("Tiempo de ejecucion: ", (fin - inicio) * 1000)

    board = cv2.imread("screenshot.png")

    detectCandies(board, candyImages)