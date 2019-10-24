#fibonacci method
def fibonacci():
    
    for i in range (0,3):
        print (i)
    a=0
    b=1
    aux =0
    print ("fibonacci 1")
    for i in range (0,10):
        print (a)
        aux = a             au0 a1 b0 au1 a1 b1 au1 a2 b1 au2 a3 b2 au3
        a=a+b
        b=aux

def fibonacci2():
    print ("fibonacci 2")
    a=0
    b=1
    for i in range (0,10):
        print ("Try number",i+1,a)
        a,b=b,a+b
fibonacci()
fibonacci2()
