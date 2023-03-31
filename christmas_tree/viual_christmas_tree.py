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

square_size = 20
height = (val+2)
width = (val*2-1)
g = screen.Screen((height*square_size,width*square_size), 1, grid=False)

# function that draw a square
def draw_square(x,y,color):
    for i in range(square_size):
        for j in range(square_size):
            g.draw_tile((y*square_size+i, x*square_size+j), color, refresh=False)

draw_square((width-1)/2,0,"yellow") # draw the little star
#for y in range(height):
    #for x in range(width):
        #g.draw_tile((y, x), "red", refresh=False)
g.refresh()

while g.wait_event()[0] != "END":
    pass
g.close()