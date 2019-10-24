#cahnge a number base 10 to base 6
#function que recivesa integer base 10 and the base you want to change. Returns a string of the new number.
def base10tobase6(num,base):
    list=[]
    while (num > base):
        list.append(num%base)
        num=int(num/base)
        if (num<=base):
            list.append(num)
    word=''
    while(len(list)>0):
        word=word+str(list.pop())
    return word

print(base10tobase6(100,6))
