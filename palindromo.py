#METHOD THAT VALIDATE IF A WORD IS PALINDROMO

def palindromo(givenString):
    size=len(givenString)/2
    j=len(givenString)-1
    band=True
    for i in range(int(size)):
        if(givenString[i]!=givenString[j]):
            band=False
            return "This is not a palindromo"
        j=j-1   
    
    if (band):
        return "This is a palindromo"
    


print(palindromo("oso"))
print(palindromo("alle"))
print(palindromo("alla"))
print(palindromo("allas"))
print(palindromo("alsla"))
print(palindromo("amor a roma"))

