#write a function that recives a num base 10 and change it to base 7 and returns the number as a string
def  base10ToBase7(num):
    res=[]
    while (num >=7):
        res.append(num % 7)
        num=int(num/7)
        if (num<7):
            res.append(num)
    #this part could be implemented better with a stack, but a let it lika that you to see how i did it the first time.
    tam=len(res)-1
    word=''
    while(tam>=0):
        word=word+str(res[tam])
        tam=tam-1
    return word
print (base10ToBase7(123))