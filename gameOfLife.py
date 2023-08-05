from time import sleep
import numpy as np
import cv2

gridSize = (100,100)
grid = np.random.randint(2,size=gridSize, dtype=np.uint8)

def game(grid):
    iterations = 2000
    it = 0
    repeatSize = 8
    cv2.namedWindow("Game Of Life")
    
    while it < iterations:
        nxGen = np.zeros(gridSize, dtype=np.uint8)
        for row,val in enumerate(grid):
            for col, v in enumerate(val): 
                nabo = 0
                for i in range(0,3):
                    for l in range(0,3):
                        if row-1+i >= 0 and col-1+l >= 0 and not (i==1 and l ==1) and row-1+i < len(grid)-1 and col-1+l < len(grid[0]):
                            if grid[row-1+i][col-1+l] == 1:
                                nabo += 1

                if 2 <= nabo <= 3 and grid[row][col] == 1:
                    nxGen[row][col] = 1
                elif nabo == 3:
                    nxGen[row][col] = 1
                elif nabo < 2 or nabo > 3:
                    nxGen[row][col] = 0
        grid = nxGen
        img = np.repeat(grid, repeatSize, axis=0).repeat(repeatSize, axis=1)
       
        cv2.imshow("Game Of Life", img*255)


        if cv2.waitKey(20) & 0xFF == 27:
            break
        it += 1
        sleep(0.1)
game(grid)
cv2.destroyAllWindows()