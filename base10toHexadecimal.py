#cahnge a number base 10 to Hexadecimal
#function que recivesa integer base 10 and the base you want to change. Returns a string of the new number.
def base10tobase6(num):
    list=[]
    while (num >= 16):
        residuo=num%16
        
        if (residuo<10):
            list.append(residuo)
        elif (residuo==10):
            list.append('A')
        elif (residuo==11):
            list.append('B')
        elif (residuo==12):
            list.append('C')
        elif (residuo==13):
            list.append('D')
        elif (residuo==14):
            list.append('E')
        else :
            list.append('F')
        num=int(num/16)
        if (num<16):
            list.append(num)
    word=''
    while (len(list)>0):
        word=word+str(list.pop())
       
    return word

print(base10tobase6(9215))
