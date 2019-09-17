#example of init method and the self constructor

class practice:
    #the __init__ method is the main method of the class and it is call every time we instance an object of this class that why the result of this program
    #we can see two diffeent names and ocupations , cuz this __init__ method is called twice and the constructor self assign memory for each variable to each object
    def __init__(self,name,ocupation):
        self.name=name
        self.ocupation=ocupation

    #here is important to notice that this method only recives the 'self' parameter
    #it is because every object created (object1 and object2) hava their own constructor and with that you can acces to the variables of each object
    def printinfo(self):
        return (self.name,self.ocupation)

object1 = practice("ileana","worker")

object2 = practice("andres","worker")

print(object1.printinfo())
print(object2.printinfo())