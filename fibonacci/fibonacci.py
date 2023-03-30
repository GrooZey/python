import sys

if(len(sys.argv)!=2):
    print("ERROR: wrong number of arguments. Try with one argument only after the function's call.")
    sys.exit()

try:
    print(int(sys.argv[1]))
except:
    print("ERROR: argument is not a number.")