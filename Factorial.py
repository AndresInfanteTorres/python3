#recursive method to do the factorial of a number
def recursiveFunction(num):
        if (num>1):
            return num * recursiveFunction(num -1)
        else:
            return 1



print (recursiveFunction(4))

