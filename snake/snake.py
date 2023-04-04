from tkdraw import screen,basic
import sys
from tkinter import *

if(len(sys.argv)!=1):
    print("ERROR: wrong number of arguments. Try with one argument only after the function's call.")
    sys.exit()

square_size = 20
height = 40
width = 60
g = screen.Screen((height,width), square_size, grid=False)

g.refresh()

while g.wait_event()[0] != "END":
    pass
g.close()