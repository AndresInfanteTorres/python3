#pilas
class pila:
    def __init__(self,lista):
        self.lista=lista
        

    def stackmanipulation(self):
        #adding an elements
        #the function range takes trhee arguments:
        #A start argument is a starting number of the sequence. i.e., lower limit. By default, it starts with 0 if not specified.
        #A stop argument is an upper limit. i.e.generate numbers up to this number, The range()  function doesn’t include this number in the result.
        #The step is a difference between each number in the result. The default value of the step is 1 if not specified.
        #the next range will start in 3 and ends in 16 with increments of 12.
        for x in range(3,16,12):
            self.lista.append(x)

        print (self.lista)
        n=self.lista.pop()
        print ("removing element: ",n)
        return self.lista

lista1=[1,2,3]

objeto1 =pila(lista1)

print(objeto1.stackmanipulation())