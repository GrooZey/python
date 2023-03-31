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

def branch_or_ball():
    c = "green"
    rnd = random.random()
    if (rnd<=0.1):
        c = "red"
    elif (rnd>0.1 and rnd<=0.2):
        c = "blue"
    return c

draw_square((width-1)/2,0,"yellow") # draw the little star
for i in range(3):
    draw_square((width-2+i)/2,height-1,"brown") 
for y in range(height-2):
    for x in range(width):
        if x>=val-1-y and x<=val+y-1:
            draw_square(x,y+1,branch_or_ball())
g.refresh()

while g.wait_event()[0] != "END":
    pass
g.close()