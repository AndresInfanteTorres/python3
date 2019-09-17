#method that check the blank spaces in a String
def blankSpaces(givenString):
    positions=[]
    band=0
    for i in givenString:
        if (i == ' '):
            positions.append(band)
        band=band+1
        
    print ("The given string has blank spaces in this positions:" )
    print(positions)


andy="Andrew is coding and debuging"
blankSpaces(andy)
    
