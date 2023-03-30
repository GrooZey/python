import sys

if(len(sys.argv)!=2):
    print("ERROR: wrong number of arguments. Try with one argument only after the function's call.")
    sys.exit()

for arg in sys.argv[1:]:
    print (arg)