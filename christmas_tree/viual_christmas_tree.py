from tkdraw import screen
import random
import sys

if(len(sys.argv)!=2):
    print("ERROR: wrong number of arguments. Try with one argument only after the function's call.")
    sys.exit()
val = 0
try:
    val = int(sys.argv[1])
except:
    print("ERROR: argument is not a number. Try with a number.")
    sys.exit()
if(val<3):
    print("ERROR: argument lower than 3. Try with a bigger value.")
    sys.exit()

square_size = 10

height = (val+2)*square_size
width = val*square_size
g = screen.Screen((height,width), 1, grid=False)

for y in range(height):
    for x in range(width):
        g.draw_tile((y, x), "red", refresh=False)
g.refresh()

g.close()