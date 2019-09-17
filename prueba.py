class andresClass:
    def imprimir(a,b):
        
        
        print (a+b)
    

    
    def numero_perfecto( num):
        
        ciclos=num/2
        numerosSumar = []
        for i in range (1,(int(ciclos))+1):
            if (num%i)==0:
                numerosSumar.append(i)
        suma=0
        for x in numerosSumar:
            suma=suma+x
            
        print (numerosSumar)
        if (num==suma):
            print ("numero perfecto")
        else:
            print ("numero imperfecto")

    def most_frecuent(given_array):
        
        print ("most frecuent function")
        max=0
        new=0
        band=0
        for x in given_array:
            for y in given_array:
                if (x==y):
                    band=band+1
            if(band>max):
                new=x
                max=band
            band=0  
       
        print ("The most frecuent number is ",new, " it repits ",max, " times.")

    

            
                
    array=[1,3,4,3,5,6,4,5,6,3,45,2,4,21,2,2,5,67,2]         
    imprimir(5,45)
    numero_perfecto(6)
    numero_perfecto(496)
    numero_perfecto(8128)
    numero_perfecto(8127)
    numero_perfecto(77)
    numero_perfecto(676)
    most_frecuent(array)
    
    
    

