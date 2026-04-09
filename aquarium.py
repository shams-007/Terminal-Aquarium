import os
import time

x = 0
y = 0
position = 1
width = 20

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    x += position

    if x >= width or x <= 0:
        position *= -1

    
    if position > 0:
        print(" " * x + "><(({*>") # Looking Right
    else:
        print(" " * x + "<*))><")  # Looking Left
    
    time.sleep(0.1)

