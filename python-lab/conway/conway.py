from copy import copy
size = 12
import time
import os
import numpy as np
field = [[np.random.choice([0,0,0,0,0,0,0,0,0,0,0,0,1]) for _ in range(20) ] for i in range(size)]

field[2][3] = 1
field[3][4] = 1
field[4][4] = 1
field[4][3] = 1
field[4][2] = 1
for i in field: print(i)
for i in range(120):
    c = [copy(i) for i in field]
    time.sleep(0.4)
    for i in range(-1, len(field) -1):
        for j in range(-1, len(field[i]) -1 ):
            neighbors = 0;
            

            neighbors += sum(field[i-1][j-1:j+2])
            neighbors += field[i][j-1]
            neighbors += field[i][j+1]
            neighbors += sum(field[i+1][j-1:j+2])
            

            #print(i + k, field[i + k][j-1:j+2])
            if neighbors == 3:
                c[i][j] = 1
            elif neighbors > 3 or neighbors < 2:
                c[i][j] = 0
    os.system("clear")            
    field = c
    for i in field:
        for k in i:
            if k == 1:
                print('\033[36m', '[#]', end='')
            else:
                print('\033[31m', '[ ]', end='')
        print('\n')

        
    
print("done")

