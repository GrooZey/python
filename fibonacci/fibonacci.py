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

if(val<1):
    print("ERROR: argument lower than 1. Try with a bigger value.")
    sys.exit()

# First value of the Fibonacci's sequence is 0 and the second is 1. The element Fn+2 = Fn+1 + Fn
def fibonacci(count):
    stock = 0
    nb1 = 0
    nb2 = 1
    for i in range(count):
        stock = nb1 + nb2
        nb1 = nb2
        nb2 = stock
    return nb1

print(fibonacci(val-1))