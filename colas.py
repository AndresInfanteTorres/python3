#colas
class cola:
    def __init__(self,lista):
        self.list=lista

    def colas(self):
        print ("Original list")
        print (self.list)
        print("Adding elements to the list")
        for x in range(5,10):
            self.list.append(x)
        print("new list")
        print (self.list)
        n=self.list.pop(0)
        print (f"extracting the first element of the list: {n}")
        n=self.list.pop(0)
        print (f"extracting the first element of the list: {n}")
        return self.list

lista1=[1,2,3]
object1=cola(lista1)

print ("final list: ",object1.colas())